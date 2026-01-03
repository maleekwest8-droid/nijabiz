import os
import shutil
import uuid
from fastapi import FastAPI, Depends, HTTPException, Query, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, database, seed_data
from database import engine, get_db

# Calculate the directory where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
UPLOAD_DIR = os.path.join(STATIC_DIR, "uploads")

# Create database tables
database.run_migrations(engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="BizBook - Nigerian Local Business Directory")

@app.on_event("startup")
def startup_event():
    db = database.SessionLocal()
    try:
        seed_data.seed_businesses(db)
    finally:
        db.close()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CRUD Endpoints

@app.get("/")
def read_root():
    # Try static/index.html first, then root index.html
    paths_to_check = [
        os.path.join(STATIC_DIR, "index.html"),
        os.path.join(BASE_DIR, "index.html")
    ]
    
    for path in paths_to_check:
        if os.path.exists(path):
            return FileResponse(path)
            
    return {
        "error": "index.html not found",
        "tip": "Ensure index.html is in your repository root or in a folder named 'static'."
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/businesses", response_model=List[schemas.Business])
def get_businesses(
    search: Optional[str] = Query(None, description="Search by name or category"),
    state: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    vacancy: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(models.Business)
    # ... filters ...
    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (models.Business.name.ilike(search_filter)) | 
            (models.Business.category.ilike(search_filter))
        )
    if state:
        query = query.filter(models.Business.state.ilike(f"%{state}%"))
    if city:
        query = query.filter(models.Business.city.ilike(f"%{city}%"))
    if vacancy:
        query = query.filter(models.Business.vacancy_status.ilike(f"%{vacancy}%"))
        
    return query.order_by(models.Business.is_featured.desc()).offset(skip).limit(limit).all()

# --- New Advanced Features Endpoints ---

@app.post("/businesses/{business_id}/click")
def register_click(business_id: int, db: Session = Depends(get_db)):
    db_business = db.query(models.Business).filter(models.Business.id == business_id).first()
    if not db_business:
        raise HTTPException(status_code=404, detail="Business not found")
    db_business.clicks_count += 1
    db.commit()
    return {"message": "Click registered", "clicks": db_business.clicks_count}

@app.get("/businesses/{business_id}/reviews", response_model=List[schemas.Review])
def get_reviews(business_id: int, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.business_id == business_id).all()

@app.post("/reviews", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    # Create the review
    db_review = models.Review(**review.dict())
    db.add(db_review)
    
    # Update business rating
    db_business = db.query(models.Business).filter(models.Business.id == review.business_id).first()
    if db_business:
        new_count = db_business.review_count + 1
        new_avg = ((db_business.average_rating * db_business.review_count) + review.rating) / new_count
        db_business.review_count = new_count
        db_business.average_rating = round(new_avg, 1)
        
    db.commit()
    db.refresh(db_review)
    return db_review

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total_businesses = db.query(models.Business).count()
    total_clicks = db.query(func.sum(models.Business.clicks_count)).scalar() or 0
    total_reviews = db.query(models.Review).count()
    avg_rating = db.query(func.avg(models.Business.average_rating)).scalar() or 0
    
    return {
        "total_businesses": total_businesses,
        "total_clicks": total_clicks,
        "total_reviews": total_reviews,
        "average_system_rating": round(avg_rating, 1) if avg_rating else 0
    }

@app.get("/stats/top-clicked", response_model=List[schemas.Business])
def get_top_clicked(limit: int = 5, db: Session = Depends(get_db)):
    return db.query(models.Business).order_by(models.Business.clicks_count.desc()).limit(limit).all()

@app.post("/upload-logo")
async def upload_logo(file: UploadFile = File(...)):
    # Create unique filename
    file_ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, "logos", filename)
    
    # Ensure logos directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"logo_url": f"/static/uploads/logos/{filename}"}

@app.get("/admin", include_in_schema=False)
def admin_page():
    return FileResponse(os.path.join(STATIC_DIR, "admin.html"))

@app.patch("/businesses/{business_id}/feature")
def toggle_feature(business_id: int, db: Session = Depends(get_db)):
    db_business = db.query(models.Business).filter(models.Business.id == business_id).first()
    if not db_business:
        raise HTTPException(status_code=404, detail="Business not found")
    db_business.is_featured = not db_business.is_featured
    db.commit()
    return {"message": "Feature status updated", "is_featured": db_business.is_featured}

@app.get("/businesses/{business_id}", response_model=schemas.Business)
def get_business(business_id: int, db: Session = Depends(get_db)):
    business = db.query(models.Business).filter(models.Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

@app.post("/businesses", response_model=schemas.Business)
def create_business(business: schemas.BusinessCreate, db: Session = Depends(get_db)):
    db_business = models.Business(**business.dict())
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business

# Serve static files
# Ensure the static directory exists
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

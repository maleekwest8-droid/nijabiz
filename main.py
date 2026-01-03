import os
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional

import models, schemas, database, seed_data
from database import engine, get_db

# Calculate the directory where main.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nigerian Local Business Directory")

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
        
    return query.offset(skip).limit(limit).all()

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

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

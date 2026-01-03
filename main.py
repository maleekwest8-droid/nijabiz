import os
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List, Optional

import models, schemas, database
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nigerian Local Business Directory")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CRUD Endpoints

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/businesses", response_model=List[schemas.Business])
def get_businesses(
    search: Optional[str] = Query(None, description="Search by name or category"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Business)
    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (models.Business.name.ilike(search_filter)) | 
            (models.Business.category.ilike(search_filter))
        )
    return query.all()

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
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

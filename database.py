import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get database URL from environment variable, default to local SQLite
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./business_directory.db")

# For SQLite, we need to handle special connection arguments
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    # Fix for newer SQLAlchemy versions with Render/Heroku Postgres URLs
    if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)
    connect_args = {}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import inspect, text

def run_migrations(engine):
    """
    Checks the database for missing columns in the 'businesses' table 
    and adds them based on the current models.
    """
    inspector = inspect(engine)
    
    # Check if 'businesses' table exists
    if 'businesses' not in inspector.get_table_names():
        return

    existing_columns = [col['name'] for col in inspector.get_columns('businesses')]
    
    # Define expected columns and their types for SQLite
    # We only need to add columns that were added AFTER the initial setup
    new_columns = {
        "region": "VARCHAR",
        "state": "VARCHAR",
        "city": "VARCHAR",
        "vacancy_status": "VARCHAR DEFAULT 'None'",
        "is_verified": "INTEGER DEFAULT 0",
        "logo_url": "VARCHAR",
        "instagram": "VARCHAR",
        "twitter": "VARCHAR",
        "facebook": "VARCHAR",
        "opening_hours": "VARCHAR",
        "google_maps_url": "VARCHAR",
        "is_featured": "INTEGER DEFAULT 0",
        "clicks_count": "INTEGER DEFAULT 0",
        "average_rating": "FLOAT DEFAULT 0.0",
        "review_count": "INTEGER DEFAULT 0"
    }

    with engine.connect() as conn:
        for column_name, column_type in new_columns.items():
            if column_name not in existing_columns:
                print(f"Adding missing column: {column_name}")
                try:
                    conn.execute(text(f"ALTER TABLE businesses ADD COLUMN {column_name} {column_type}"))
                    conn.commit()
                except Exception as e:
                    print(f"Error adding {column_name}: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

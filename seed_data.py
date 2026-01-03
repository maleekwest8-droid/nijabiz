from sqlalchemy.orm import Session
import models

def seed_businesses(db: Session):
    # Check if we already have a large dataset
    if db.query(models.Business).count() > 10:
        return

    # Clear existing to ensure clean categorized data
    db.query(models.Business).delete()
    db.query(models.Review).delete()

    businesses = [
        # --- FEATURED BUSINESSES ---
        {
            "name": "Slot Systems (Featured)",
            "category": "Retail & Tech",
            "phone": "+234700756864", "whatsapp": "234700756864",
            "address": "Ikeja & Lekki, Lagos",
            "description": "Premium gadget retailer. Verified and Featured.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Slot",
            "instagram": "slot_ng", "twitter": "slot_ng", "facebook": "slotnigeria",
            "opening_hours": "Mon-Sat 9am-6pm",
            "google_maps_url": "https://maps.google.com"
        },
        {
            "name": "Nowoola Palace Hotels & Suites",
            "category": "Hospitality",
            "phone": "+2349043042218", "whatsapp": "",
            "address": "Victoria Island, Lagos",
            "description": "Luxurious stay in the heart of VI. Now Hiring!",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "Vacancy Available", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Nowoola",
            "instagram": "nowoola_hotels",
            "opening_hours": "24/7",
            "google_maps_url": "https://maps.google.com"
        },
        
        # --- REGULAR CATEGORIZED ---
        {
            "name": "ArewaTecHub Kano",
            "category": "Tech Hub",
            "phone": "+2348066677856", "whatsapp": "2348066677856",
            "address": "Gwarzo Road, Kano",
            "description": "Tech skills training and co-working.",
            "region": "North West", "state": "Kano", "city": "Kano",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Arewa",
            "instagram": "arewa_tech", "twitter": "arewa_tech"
        },
        {
            "name": "Asia Town Port Harcourt",
            "category": "Fine Dining",
            "phone": "+2348186622153", "whatsapp": "2348186622153",
            "address": "Old GRA, Port Harcourt",
            "description": "Elite Asian restaurant.",
            "region": "South South", "state": "Rivers", "city": "Port Harcourt",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Asia",
            "instagram": "asiatownph",
            "opening_hours": "12pm-11pm"
        },
        {
            "name": "MTN Nigeria HQ",
            "category": "Telecommunications",
            "phone": "+2348031234567", "whatsapp": "2348031234567",
            "address": "Ikoyi, Lagos",
            "description": "Everywhere you go.",
            "region": "South West", "state": "Lagos", "city": "Ikoyi",
            "vacancy_status": "Vacancy Available", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=MTN",
            "facebook": "MTNLoaded"
        }
    ]

    for biz in businesses:
        db_business = models.Business(**biz)
        db.add(db_business)
    
    db.commit()
    print(f"Successfully seeded {len(businesses)} enriched businesses!")

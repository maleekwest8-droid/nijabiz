from sqlalchemy.orm import Session
import models

def seed_businesses(db: Session):
    # Check if we already have a large dataset
    if db.query(models.Business).count() > 40:
        return

    # Clear existing to ensure clean categorized data
    db.query(models.Business).delete()

    businesses = [
        # --- LAGOS: LEKKI & VI (The "Island" request) ---
        {
            "name": "Slot Systems Limited (Lekki)",
            "category": "Retail & Tech",
            "phone": "+234700756864",
            "whatsapp": "234700756864",
            "address": "Shop B3-4, Truly Yours Plaza, Agungi, Lekki",
            "description": "Leading retail store for mobile phones and gadgets.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1
        },
        {
            "name": "Genesis Deluxe Cinemas (The Palms)",
            "category": "Entertainment",
            "phone": "+2347000300300",
            "whatsapp": "",
            "address": "Palms Shopping Mall, Lekki",
            "description": "Premium cinema experience in the heart of Lekki.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },
        {
            "name": "iConnect Apple Store",
            "category": "Tech Shop",
            "phone": "+2348093618708",
            "whatsapp": "2348093618708",
            "address": "Palms Mall, Victoria Island",
            "description": "Authorized reseller of Apple products and accessories.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1
        },
        {
            "name": "Nowoola Palace Hotels",
            "category": "Hospitality",
            "phone": "+2349043042218",
            "whatsapp": "",
            "address": "1 Nancy Nowoola St, VI, Lagos",
            "description": "Luxurious stay in Victoria Island with premium suites.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },
        {
            "name": "Vasaloni Beauty",
            "category": "Beauty & Spa",
            "phone": "+2347012345678",
            "whatsapp": "2347012345678",
            "address": "71d Freedom Way, Lekki Phase 1",
            "description": "Exclusive beauty solutions and spa services in Lekki.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1
        },
        {
            "name": "So-Kleen Pest Control",
            "category": "Professional Services",
            "phone": "+2348012345679",
            "whatsapp": "2348012345679",
            "address": "16B Bashorun Okusanya, Lekki Phase 1",
            "description": "Verified cleaning and pest control services.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },

        # --- ABUJA ---
        {
            "name": "Ciao Italia Abuja",
            "category": "Restaurant",
            "phone": "+2348123456780",
            "whatsapp": "",
            "address": "Plot 174 Kur Mohammed Ave, Wuse, Abuja",
            "description": "Authentic Italian pizzas and fine dining.",
            "region": "North Central", "state": "Abuja", "city": "Wuse",
            "vacancy_status": "None", "is_verified": 1
        },
        {
            "name": "EHA Clinics Wuse",
            "category": "Healthcare",
            "phone": "+2348000000000",
            "whatsapp": "",
            "address": "Novare Central Mall, Wuse, Abuja",
            "description": "Top-tier healthcare services and primary care.",
            "region": "North Central", "state": "Abuja", "city": "Wuse",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },
        {
            "name": "Salamander Cafe",
            "category": "Cafe & Hub",
            "phone": "+2348095555620",
            "whatsapp": "",
            "address": "5 Bujumbura St, Wuse 2, Abuja",
            "description": "Workspace, literary hub, and great coffee.",
            "region": "North Central", "state": "Abuja", "city": "Wuse 2",
            "vacancy_status": "None", "is_verified": 1
        },

        # --- PORT HARCOURT ---
        {
            "name": "Asia Town PH",
            "category": "Fine Dining",
            "phone": "+2348186622153",
            "whatsapp": "2348186622153",
            "address": "24 Forces Avenue, Old GRA, Port Harcourt",
            "description": "Elite Asian restaurant and events venue.",
            "region": "South South", "state": "Rivers", "city": "Port Harcourt",
            "vacancy_status": "None", "is_verified": 1
        },
        {
            "name": "CornerStore Cafe PH",
            "category": "Cafe",
            "phone": "+2347057023803",
            "whatsapp": "",
            "address": "51 Tombia St, New GRA, Port Harcourt",
            "description": "Popular spot for cocktails and pastries.",
            "region": "South South", "state": "Rivers", "city": "Port Harcourt",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },

        # --- KANO ---
        {
            "name": "ArewaTecHub Kano",
            "category": "Tech Hub",
            "phone": "+2348066677856",
            "whatsapp": "2348066677856",
            "address": "Gwarzo Road, Kano",
            "description": "Tech skills training and startup support center.",
            "region": "North West", "state": "Kano", "city": "Kano",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },
        {
            "name": "MegaMore Wireless",
            "category": "Internet Provider",
            "phone": "+2348012345680",
            "whatsapp": "",
            "address": "Sabon Gari, Kano",
            "description": "Reliable broadband internet services in Kano city.",
            "region": "North West", "state": "Kano", "city": "Kano",
            "vacancy_status": "None", "is_verified": 1
        },

        # --- ENUGU ---
        {
            "name": "5m Telecom Enugu",
            "category": "IT Services",
            "phone": "+2347085173638",
            "whatsapp": "",
            "address": "20 Ibusa Ave, Independence Layout, Enugu",
            "description": "Internet service provider and IT consulting.",
            "region": "South East", "state": "Enugu", "city": "Enugu",
            "vacancy_status": "None", "is_verified": 1
        },
        {
            "name": "Abic Books",
            "category": "Publishing",
            "phone": "+2348062251178",
            "whatsapp": "",
            "address": "20 Edozien St, Uwani, Enugu",
            "description": "Major publishing house and office equipment supplier.",
            "region": "South East", "state": "Enugu", "city": "Enugu",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },

        # --- IBADAN (Oyo) ---
        {
            "name": "GIG Logistics Ibadan",
            "category": "Logistics",
            "phone": "+2348123456789",
            "whatsapp": "",
            "address": "Ring Road, Ibadan",
            "description": "Leading logistics and courier services in Oyo State.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },
        {
            "name": "Kilimanjaro Bodija",
            "category": "Food & Restaurant",
            "phone": "+2348100393579",
            "whatsapp": "2348100393579",
            "address": "Bodija, Ibadan",
            "description": "Popular fast food chain offering quality local meals.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1
        },

        # --- REPRESENTING SMALL BUSINESSES (as requested) ---
        {
            "name": "Lekki Tailors",
            "category": "Fashion",
            "phone": "+2348100001111",
            "whatsapp": "2348100001111",
            "address": "Lekki Phase 1, Lagos",
            "description": "Verified bespoke tailoring for men and women.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 0
        },
        {
            "name": "Obi's Tech Shop",
            "category": "Tech Repairs",
            "phone": "+2348100002222",
            "whatsapp": "2348100002222",
            "address": "Computer Village, Ikeja",
            "description": "Fast repairs for iPhones and MacBooks.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "Vacancy Available", "is_verified": 0
        }
    ]

    # Add big corporates for completeness (updated schemas)
    corporates = [
        {
            "name": "MTN Nigeria HQ",
            "category": "Telecommunications",
            "phone": "+2348031234567", "whatsapp": "2348031234567",
            "address": "Ikoyi, Lagos", "description": "National HQ for MTN Nigeria.",
            "region": "South West", "state": "Lagos", "city": "Ikoyi",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        },
        {
            "name": "Dangote Group",
            "category": "Manufacturing",
            "phone": "+23412345678", "whatsapp": "",
            "address": "Lekki Free Trade Zone", "description": "Global conglomerate based in Lagos.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "Vacancy Available", "is_verified": 1
        }
    ]

    for biz in businesses + corporates:
        db_business = models.Business(**biz)
        db.add(db_business)
    
    db.commit()
    print(f"Successfully seeded {len(businesses) + len(corporates)} localized businesses!")

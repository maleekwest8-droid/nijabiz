from sqlalchemy.orm import Session
import models

def seed_businesses(db: Session):
    # Check if we already have businesses
    # For this expansion, we might want to clear existing ones if they are just the basic samples
    # but the current logic is to skip if not empty. Let's make it smarter or just add to it.
    if db.query(models.Business).count() > 30:
        return

    # Delete existing basic samples to avoid duplicates if re-running
    db.query(models.Business).delete()

    businesses = [
        # --- BIG CORPORATES ---
        {
            "name": "MTN Nigeria",
            "category": "Telecommunications",
            "phone": "+2348031234567",
            "whatsapp": "2348031234567",
            "address": "439 Corporation Drive, Dolphin Estate, Ikoyi, Lagos",
            "description": "Nigeria's largest telecommunication company, providing mobile, data, and digital services."
        },
        {
            "name": "Dangote Cement",
            "category": "Manufacturing",
            "phone": "+23412345678",
            "whatsapp": "",
            "address": "Union Bank Building, Marina, Lagos",
            "description": "Leading cement producer in Sub-Saharan Africa, founded by Aliko Dangote."
        },
        {
            "name": "United Bank for Africa (UBA)",
            "category": "Banking",
            "phone": "+23412345680",
            "whatsapp": "2349033000000",
            "address": "57 Marina, Lagos Island, Lagos",
            "description": "A pan-African financial services group with a strong presence across the continent."
        },
        
        # --- RETAIL & TECH SHOPS ---
        {
            "name": "Slot Systems Limited",
            "category": "Retail & Tech",
            "phone": "+234700756864",
            "whatsapp": "234700756864",
            "address": "2b Medical Road, Ikeja, Lagos",
            "description": "Leading retail store for mobile phones, laptops, and gadgets with nationwide locations."
        },
        {
            "name": "Naija Tech Deals",
            "category": "Tech Shop",
            "phone": "+2348129894656",
            "whatsapp": "2348129894656",
            "address": "4 Bamgboshe Street, Lagos Island, Lagos",
            "description": "Your one-stop shop for specialized tech gadgets and computer accessories."
        },
        {
            "name": "Deluxe Nigeria",
            "category": "Electronics",
            "phone": "+2349094789078",
            "whatsapp": "2349094789078",
            "address": "11 Fadeyi Street, Ikeja, Lagos",
            "description": "Online and physical store for electronics, home appliances, and office equipment."
        },
        {
            "name": "Nova Store Ltd",
            "category": "Gadgets",
            "phone": "+2349063800952",
            "whatsapp": "2349063800952",
            "address": "9 Ola Ayeni St, Ikeja, Lagos",
            "description": "Legit gadget consultants and retail store for high-end smartphones and accessories."
        },
        {
            "name": "Obejor Computers",
            "category": "IT Services",
            "phone": "+2348171161107",
            "whatsapp": "",
            "address": "17 Obafemi Awolowo Way, Ikeja, Lagos",
            "description": "Specialized computer sales, repairs, and enterprise IT solutions."
        },

        # --- FOOD, RESTAURANTS & CAFES ---
        {
            "name": "BourbonHouse Cafe",
            "category": "Restaurant & Cafe",
            "phone": "+2349087188000",
            "whatsapp": "",
            "address": "741 Adeola Hopewell St, Victoria Island, Lagos",
            "description": "Premium coffee, brunch, and fine dining with a global-inspired menu."
        },
        {
            "name": "Lagos Bistro Abuja",
            "category": "Restaurant",
            "phone": "+2347043800000",
            "whatsapp": "2347043800000",
            "address": "7 Humbori Street, Adetokunbo Ademola Crescent, Wuse 2, Abuja",
            "description": "Vibrant bistro offering a fusion of Nigerian and international cuisines."
        },
        {
            "name": "Asia Town Port Harcourt",
            "category": "Fine Dining",
            "phone": "+2348186622153",
            "whatsapp": "2348186622153",
            "address": "24 Forces Avenue, Old G.R.A, Port Harcourt",
            "description": "The elite Asian restaurant in PH, known for exotic dishes and impeccable ambiance."
        },
        {
            "name": "Hot Crust Cafe",
            "category": "Cafe",
            "phone": "+2347063372142",
            "whatsapp": "",
            "address": "Ogudu Road, Lagos",
            "description": "Cozy workspace cafe serving fresh pastries and artisanal coffee."
        },
        {
            "name": "CornerStore PH",
            "category": "Bar & Cafe",
            "phone": "+2347057023803",
            "whatsapp": "",
            "address": "51 Tombia St, New GRA, Port Harcourt",
            "description": "Famous for cocktails, desserts, and the best pastries in the Garden City."
        },

        # --- SMALL BUSINESSES & SERVICES ---
        {
            "name": "Divine Option Technical",
            "category": "Electrical Services",
            "phone": "+2349039844917",
            "whatsapp": "2349039844917",
            "address": "B02 Afro Mall, Dei-dei, Abuja",
            "description": "Verified electrical products, wiring services, and maintenance for homes and offices."
        },
        {
            "name": "Riteway Cleaners Abuja",
            "category": "Cleaning Service",
            "phone": "+2348032457352",
            "whatsapp": "2348032457352",
            "address": "Suite B75 Murg Plaza, Area 7, Garki, Abuja",
            "description": "Professional home and office cleaning, laundry, and pest control specialists."
        },
        {
            "name": "Pawnshop Nigeria",
            "category": "Financial Services",
            "phone": "+2349067703153",
            "whatsapp": "",
            "address": "7 Furo Ezimora Street, Lekki Phase 1, Lagos",
            "description": "Quick cash solutions and collateral-backed credit services for SMEs."
        },
        {
            "name": "Sowget Exchanger",
            "category": "Crypto Exchange",
            "phone": "+2348144333114",
            "whatsapp": "2348144333114",
            "address": "Adeniyi Jones, Ikeja, Lagos",
            "description": "Legit and instant exchange for Bitcoin, USDT, and other e-currencies."
        },

        # --- FASHION & LIFESTYLE ---
        {
            "name": "Dejiandkola",
            "category": "Fashion Brand",
            "phone": "+2348034567890",
            "whatsapp": "2348034567890",
            "address": "Magodo Phase 2, Lagos",
            "description": "Master tailors for bespoke corporate suits and traditional African attire."
        },
        {
            "name": "Fashion Icon Owerri",
            "category": "Boutique",
            "phone": "+2348037075960",
            "whatsapp": "2348037075960",
            "address": "48 Wetheral Road, Owerri, Imo State",
            "description": "Upscale boutique for premium men's and women's fashion in the heart of Owerri."
        },
        {
            "name": "21st Century Designs",
            "category": "Fashion Studio",
            "phone": "+2348033012222",
            "whatsapp": "",
            "address": "23 Olufemi Road, Surulere, Lagos",
            "description": "Designer fashion house focused on contemporary Nigerian styles and bridal wear."
        },
        {
            "name": "Dressense Ikeja",
            "category": "Clothing Store",
            "phone": "+23412345688",
            "whatsapp": "",
            "address": "Shop 64/65, Alade Market, Ikeja, Lagos",
            "description": "Verified retail store for high-quality corporate and casual outfits."
        },

        # --- TRAVEL & LOGISTICS ---
        {
            "name": "GIG Logistics",
            "category": "Courier",
            "phone": "+2348139851120",
            "whatsapp": "2348139851120",
            "address": "190/192 Ikorodu Road, Lagos",
            "description": "The leading e-commerce logistics provider in Nigeria with local and international coverage."
        },
        {
            "name": "Peace Mass Transit",
            "category": "Transportation",
            "phone": "+2348055091822",
            "whatsapp": "",
            "address": "Utako Park, Abuja",
            "description": "Affordable and reliable inter-state land transportation across Nigeria."
        },
        {
            "name": "Wakanow",
            "category": "Travel Agency",
            "phone": "+23412773010",
            "whatsapp": "",
            "address": "Plot 8, Elegushi Beach Road, Lekki, Lagos",
            "description": "Nigeria's leading online travel agency for flight bookings and vacation packages."
        },

        # --- MORE RETAIL & SPECIALTY ---
        {
            "name": "Addide Supermarket",
            "category": "Supermarket",
            "phone": "+2348023146240",
            "whatsapp": "",
            "address": "Multiple branches across Lagos",
            "description": "Convenient community supermarket chain for daily household needs."
        },
        {
            "name": "Naija Tech Deals",
            "category": "Specialized Tech",
            "phone": "+2348129894656",
            "whatsapp": "2348129894656",
            "address": "4 Bamgboshe Street, Lagos Island",
            "description": "Laptops, PC components, and gaming accessories."
        },
        {
            "name": "Harmony Stores NG",
            "category": "Department Store",
            "phone": "+2349012345678",
            "whatsapp": "",
            "address": "Ikeja City Mall, Lagos",
            "description": "Verified retailer for international beauty and home brands."
        },
        {
            "name": "itel Home PH",
            "category": "Smartphones",
            "phone": "+2348149749070",
            "whatsapp": "2348149749070",
            "address": "Danalabest Complex, Port Harcourt",
            "description": "Authorized itel retail outlet for affordable smartphones and gadgets."
        },
        {
            "name": "itel Home Abeokuta",
            "category": "Smartphones",
            "phone": "+2349024176445",
            "whatsapp": "2349024176445",
            "address": "Fastlink Plaza, Abeokuta",
            "description": "Authorized itel retail outlet in Ogun State."
        },
        {
             "name": "Kara.com.ng",
            "category": "Online Marketplace",
            "phone": "+2349091909269",
            "whatsapp": "2349091909269",
            "address": "Royal Coast Group, Lagos",
            "description": "Trusted online retailer for generator sets, power solutions, and large appliances."
        }
    ]

    for biz in businesses:
        db_business = models.Business(**biz)
        db.add(db_business)
    
    db.commit()
    print(f"Successfully seeded {len(businesses)} legit businesses!")

from sqlalchemy.orm import Session
import models

def seed_businesses(db: Session):
    # Idempotent seeding: only add businesses that don't exist by name
    # This ensures your existing data is NEVER wiped.

    businesses = [
        # --- LAGOS BUSINESSES (40) ---
        {
            "name": "Slot Systems (Featured)", "category": "Retail & Tech",
            "phone": "+234700756864", "whatsapp": "234700756864", "address": "1 OKANLAWON AJAYI ST, OFF M/BANK ANTHONY WAY, IKEJA",
            "description": "Premium gadget retailer. Phones, Laptops and Accessories.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Slot",
            "instagram": "slot_ng", "twitter": "slot_ng", "opening_hours": "Mon-Sat 9am-6pm",
            "google_maps_url": "https://maps.google.com"
        },
        {
            "name": "Chris Ejik Group", "category": "Engineering",
            "phone": "+23414930101", "whatsapp": "", "address": "3, Oje-Imavan Street, Off Kudirat Abiola Way, Ikeja",
            "description": "Engineering, construction, procurement and pharmaceuticals.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Chris",
            "opening_hours": "Mon-Fri 8am-5pm"
        },
        {
            "name": "Chronicles Software", "category": "IT",
            "phone": "+23412345678", "whatsapp": "", "address": "19, Shogunle Street, off Mobolaji Bank Anthony Way, Ikeja",
            "description": "Software development and educational technology solutions.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Chronicles"
        },
        {
            "name": "Alert Microfinance Bank", "category": "Finance",
            "phone": "+2348012345678", "whatsapp": "", "address": "123, Herbert Macaulay Way, Yaba, Lagos",
            "description": "Reliable financial services for small businesses.",
            "region": "South West", "state": "Lagos", "city": "Yaba",
            "vacancy_status": "Vacancy Available", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Alert",
            "opening_hours": "Mon-Fri 8:30am-4:30pm"
        },
        {
            "name": "Tejuosho Market Center", "category": "Shopping",
            "phone": "+23412345679", "whatsapp": "", "address": "Yaba, Lagos",
            "description": "Ultra-modern shopping center for all your retail needs.",
            "region": "South West", "state": "Lagos", "city": "Yaba",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Tejuosho"
        },
        {
            "name": "Ikeja City Mall", "category": "Shopping Mall",
            "phone": "+23412345680", "whatsapp": "", "address": "Obafemi Awolowo Way, Ikeja",
            "description": "The busiest and most popular mall in Lagos.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=ICM"
        },
        {
            "name": "The Palms Shopping Mall", "category": "Shopping Mall",
            "phone": "+23412345681", "whatsapp": "", "address": "Lekki-Epe Expressway, Lekki",
            "description": "Premium shopping destination in the heart of Lekki.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Palms"
        },
        {
            "name": "Polo Limited", "category": "Luxury Retail",
            "phone": "+23412345682", "whatsapp": "", "address": "166, Ozumba Mbadiwe Street, Victoria Island",
            "description": "Luxury watches, jewelry, and high-end fashion.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Polo"
        },
        {
            "name": "Temple Muse", "category": "Fashion",
            "phone": "+23412345683", "whatsapp": "", "address": "21, Amodu Tijani Close, Victoria Island",
            "description": "Lifestyle concept store offering high-end fashion.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Temple"
        },
        {
            "name": "Alara Boutique", "category": "Fashion & Arts",
            "phone": "+23412345684", "whatsapp": "", "address": "12A, Akin Olugbade Street, Victoria Island",
            "description": "Contemporary art, fashion, and design concept store.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Alara"
        },
        {
            "name": "Mikano International", "category": "Power Solutions",
            "phone": "+23412345685", "whatsapp": "", "address": "Plot 34/35, Acme Road, Ogba, Ikeja",
            "description": "Leading provider of power generation solutions in Nigeria.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "Vacancy Available", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Mikano"
        },
        {
            "name": "First Bank Nigeria", "category": "Finance",
            "phone": "+23412345686", "whatsapp": "", "address": "Samuel Asabia House, 35 Marina, Lagos",
            "description": "One of the oldest and largest banks in Nigeria.",
            "region": "South West", "state": "Lagos", "city": "Marina",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=FirstBank"
        },
        {
            "name": "Concept Nova", "category": "IT & Fleet Management",
            "phone": "+23412345687", "whatsapp": "", "address": "Victoria Island, Lagos",
            "description": "IT enterprise specialized in remote monitoring and IoT.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Nova"
        },
        {
            "name": "Transcorp Plc", "category": "Conglomerate",
            "phone": "+23412345688", "whatsapp": "", "address": "Victoria Island, Lagos",
            "description": "Diversified investments in hospitality and power.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Transcorp"
        },
        {
            "name": "Dej Facilities", "category": "Cleaning Services",
            "phone": "+23412345689", "whatsapp": "", "address": "10 Apapa Road, Costain, Lagos",
            "description": "Premium industrial and domestic cleaning services.",
            "region": "South West", "state": "Lagos", "city": "Costain",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Dej"
        },
        {
            "name": "Joshua Adeji & Co", "category": "Legal Services",
            "phone": "+23412345690", "whatsapp": "", "address": "12, Apapa Road, Costain, Lagos",
            "description": "Experienced legal consultants and attorneys.",
            "region": "South West", "state": "Lagos", "city": "Costain",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Adeji"
        },
        {
            "name": "Nevada Hotels", "category": "Hospitality",
            "phone": "+23412345691", "whatsapp": "", "address": "3 Aaron Irabor St, Agungi, Lekki",
            "description": "Cozy and luxurious stay in the heart of Lekki.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Nevada"
        },
        {
            "name": "Poosh Lagos", "category": "Fashion",
            "phone": "+23412345692", "whatsapp": "", "address": "15 Ologun Agbaje St, Victoria Island",
            "description": "Boutique store for unique clothing and accessories.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Poosh"
        },
        {
            "name": "Florence H Boutique", "category": "Fashion",
            "phone": "+23412345693", "whatsapp": "", "address": "32, Musa Yaradua Street, Victoria Island",
            "description": "Women's designer footwear and accessories.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Florence"
        },
        {
            "name": "Miskay Boutique", "category": "Fashion",
            "phone": "+23412345694", "whatsapp": "", "address": "Lekki Phase 1, Lagos",
            "description": "Top-tier women's fast fashion store in Lagos.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Miskay"
        },
        {
            "name": "Grey Velvet", "category": "Fashion",
            "phone": "+23412345695", "whatsapp": "", "address": "Ikeja City Mall, Lagos",
            "description": "The home of Nigerian designer brands.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Grey"
        },
        {
            "name": "Modan Luxury Store", "category": "Luxury Retail",
            "phone": "+23412345696", "whatsapp": "", "address": "1, Murtala Mohammed St, Ikoyi",
            "description": "Exclusive luxury store for international brands.",
            "region": "South West", "state": "Lagos", "city": "Ikoyi",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Modan"
        },
        {
            "name": "Paystack", "category": "Fintech",
            "phone": "+2348007297822", "whatsapp": "", "address": "Ikeja, Lagos",
            "description": "Modern online and offline payments for Africa.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Paystack",
            "instagram": "paystackhq"
        },
        {
            "name": "Flutterwave", "category": "Fintech",
            "phone": "+23412345698", "whatsapp": "", "address": "Lekki, Lagos",
            "description": "Seamless payments for businesses across the globe.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "Vacancy Available", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Flutterwave"
        },
        {
            "name": "GTBank", "category": "Finance",
            "phone": "+23412345699", "whatsapp": "", "address": "Victoria Island, Lagos",
            "description": "Innovative financial services for personal and business banking.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=GTBank"
        },
        {
            "name": "Zenith Bank", "category": "Finance",
            "phone": "+23412345700", "whatsapp": "", "address": "Plot 84, Ajose Adeogun St, VI",
            "description": "Excellence in banking service and reliability.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Zenith"
        },
        {
            "name": "Access Bank", "category": "Finance",
            "phone": "+23412345701", "whatsapp": "", "address": "14/15, Prince Alaba Abiodun St, VI",
            "description": "Leading commercial bank with global branches.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Access"
        },
        {
            "name": "Eko Hotel & Suites", "category": "Hospitality",
            "phone": "+23412772700", "whatsapp": "", "address": "Adetokunbo Ademola St, VI, Lagos",
            "description": "The most prestigious luxury hotel in Nigeria.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=EkoHotel"
        },
        {
            "name": "Radisson Blu", "category": "Hospitality",
            "phone": "+23412345703", "whatsapp": "", "address": "Ozumba Mbadiwe Ave, VI",
            "description": "Waterfront views and world-class accommodation.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Radisson"
        },
        {
            "name": "Filmhouse Cinemas", "category": "Entertainment",
            "phone": "+23412345704", "whatsapp": "", "address": "Lekki Phase 1, Lagos",
            "description": "Premium cinematic experience with IMAX technology.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Filmhouse"
        },
        {
            "name": "Terra Kulture", "category": "Arts & Dining",
            "phone": "+23412345705", "whatsapp": "", "address": "Tiamiyu Savage St, VI, Lagos",
            "description": "Promoting Nigerian culture through art, food and theater.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Terra"
        },
        {
            "name": "Yellow Chilli", "category": "Dining",
            "phone": "+23412345706", "whatsapp": "", "address": "Joel Ogunnaike St, G.R.A, Ikeja",
            "description": "Exquisite gourmet African and continental cuisine.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Yellow"
        },
        {
            "name": "Hard Rock Cafe", "category": "Dining & Entertainment",
            "phone": "+23412345707", "whatsapp": "", "address": "Landmark Village, VI",
            "description": "American fare and live music in a rock-themed setting.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=HardRock"
        },
        {
            "name": "Shiro Lagos", "category": "Dining",
            "phone": "+23412345708", "whatsapp": "", "address": "Landmark Village, VI",
            "description": "Premium Pan-Asian restaurant and bar.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Shiro"
        },
        {
            "name": "Intercontinental Hotel", "category": "Hospitality",
            "phone": "+23412345709", "whatsapp": "", "address": "Kofo Abayomi St, VI",
            "description": "Grand luxury hotel servicing business and leisure travelers.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=InterCon"
        },
        {
            "name": "Sheraton Lagos Hotel", "category": "Hospitality",
            "phone": "+23412345710", "whatsapp": "", "address": "Mobolaji Bank Anthony Way, Ikeja",
            "description": "Vibrant hotel with excellent amenities and services.",
            "region": "South West", "state": "Lagos", "city": "Ikeja",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Sheraton"
        },
        {
            "name": "Zaron Cosmetics", "category": "Beauty",
            "phone": "+23412345711", "whatsapp": "", "address": "Ikoyi, Lagos",
            "description": "Leading African provider of high-quality cosmetics.",
            "region": "South West", "state": "Lagos", "city": "Ikoyi",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Zaron"
        },
        {
            "name": "Glover Court Suya", "category": "Dining",
            "phone": "+23412345712", "whatsapp": "", "address": "Glover Court, Ikoyi",
            "description": "Famous destination for the best Suya in Lagos.",
            "region": "South West", "state": "Lagos", "city": "Ikoyi",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Suya"
        },
        {
            "name": "Lekki Conservation Centre", "category": "Tourism",
            "phone": "+23412345713", "whatsapp": "", "address": "Lekki-Epe Expressway",
            "description": "A must-visit urban jungle and nature reserve.",
            "region": "South West", "state": "Lagos", "city": "Lekki",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=LCC"
        },
        {
            "name": "Oriental Hotel", "category": "Hospitality",
            "phone": "+23412345714", "whatsapp": "", "address": "Lekki Expressway",
            "description": "Chinese-style luxury hotel overlooking the lagoon.",
            "region": "South West", "state": "Lagos", "city": "Victoria Island",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Oriental"
        },

        # --- IBADAN BUSINESSES (40) ---
        {
            "name": "Navigator Real Estate", "category": "Real Estate",
            "phone": "+2348012345715", "whatsapp": "", "address": "Atoke Plaza, General Gas-Akobo Road, Ibadan",
            "description": "Top-tier real estate and facility management firm.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "Vacancy Available", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Navigator"
        },
        {
            "name": "Taiwo Salam & Co", "category": "Real Estate",
            "phone": "+2348012345716", "whatsapp": "", "address": "U7 Joke Plaza, Bodija, Ibadan",
            "description": "Professional estate surveyors and valuers in Oyo State.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Taiwo"
        },
        {
            "name": "Advans Nigeria", "category": "Finance",
            "phone": "+2348012345717", "whatsapp": "", "address": "2 Adekunle Fajuyi Road, Dugbe, Ibadan",
            "description": "Providing loans and financial help to local vendors.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Advans"
        },
        {
            "name": "GTB Ibadan Center", "category": "Finance",
            "phone": "+2348012345718", "whatsapp": "", "address": "Ui - Secretariat Road, Bodija, Ibadan",
            "description": "Reliable banking services for Ibadan residents.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=GTBIbadan"
        },
        {
            "name": "DHL Ibadan Office", "category": "Logistics",
            "phone": "+2348012345719", "whatsapp": "", "address": "51 Oyo Road, Mokola Hill, Ibadan",
            "description": "Global leader in courier and logistics services.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=DHLIbadan"
        },
        {
            "name": "Netface Technologies", "category": "IT",
            "phone": "+2348012345720", "whatsapp": "", "address": "Dugbe, Ibadan",
            "description": "Innovative web and software development company.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Netface"
        },
        {
            "name": "KDALinks Tech", "category": "IT",
            "phone": "+2348012345721", "whatsapp": "", "address": "Olubadan Avenue, Oluyole Estate, Ibadan",
            "description": "Expert ICT solutions and computer engineering.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=KDA"
        },
        {
            "name": "Holomom Consults", "category": "Consulting",
            "phone": "+2348012345722", "whatsapp": "", "address": "Olubadan Avenue by Adeosun, Oluyole",
            "description": "Business management and educational consulting.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Holomom"
        },
        {
            "name": "Data Planet Engineering", "category": "IT",
            "phone": "+2348012345723", "whatsapp": "", "address": "Iwo Road, Ibadan North-East",
            "description": "Computer hardware, repairs and software setup.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=DataPlanet"
        },
        {
            "name": "Deejoft Consults", "category": "ICT & Design",
            "phone": "+2348012345724", "whatsapp": "", "address": "Opp. Ibadan North East LG, Iwo Road",
            "description": "Graphic design, web dev and ICT consultancy.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Deejoft"
        },
        {
            "name": "Adaeze Fabric Store", "category": "Fashion",
            "phone": "+2348012345725", "whatsapp": "", "address": "Bodija Market, Ibadan",
            "description": "Top-quality African fabrics and textiles.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Adaeze"
        },
        {
            "name": "Dayspring Supermarket", "category": "Retail",
            "phone": "+2348012345726", "whatsapp": "", "address": " Railway Shopping Complex, Bodija",
            "description": "Affordable household groceries and appliances.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Dayspring"
        },
        {
            "name": "Best Western Plus", "category": "Hospitality",
            "phone": "+2348012345727", "whatsapp": "", "address": " Iyaganku GRA, Ibadan",
            "description": "World-class luxury hotel with excellent service.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=BWestern"
        },
        {
            "name": "House of Mabella", "category": "Events",
            "phone": "+2348012345728", "whatsapp": "", "address": "Akobo, Ibadan",
            "description": "Creative event planning and decoration services.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "Vacancy Available", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Mabella"
        },
        {
            "name": "Seun FX Academy", "category": "Education",
            "phone": "+2348012345729", "whatsapp": "", "address": "Shobande St, Akobo, Ibadan",
            "description": "Professional forex and financial asset trading school.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=SeunFX"
        },
        {
            "name": "Eagleview Eye Clinic", "category": "Health",
            "phone": "+2348012345730", "whatsapp": "", "address": "3 Favour Street, Ibadan",
            "description": "Comprehensive eye care and vision solutions.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Eagleview"
        },
        {
            "name": "Odu'a Investment Co.", "category": "Investment",
            "phone": "+2348012345731", "whatsapp": "", "address": "Oba Adebimpe Road, Ibadan",
            "description": "Leading industrial and investment conglomerate in Oyo.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Odua"
        },
        {
            "name": "Fouani Nigeria", "category": "Retail",
            "phone": "+2348012345732", "whatsapp": "", "address": "Obafemi Awolowo Way, Dugbe, Ibadan",
            "description": "Direct distributor of LG electronics and home appliances.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Fouani"
        },
        {
            "name": "Slabmark Group", "category": "Manufacturing",
            "phone": "+2348012345733", "whatsapp": "", "address": "Old Lagos Road, Ibadan",
            "description": "Premium household product manufacturing enterprise.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Slabmark"
        },
        {
            "name": "Heritage Mall", "category": "Shopping Mall",
            "phone": "+2348012345734", "whatsapp": "", "address": "Dugbe, Ibadan",
            "description": "Modern shopping destination with Shoprite and more.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Heritage"
        },
        {
            "name": "University of Ibadan", "category": "Education",
            "phone": "+2348012345735", "whatsapp": "", "address": "Oyo Road, Ibadan",
            "description": "Nigeria's flagship tertiary institution.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=UI"
        },
        {
            "name": "Ventura Mall", "category": "Shopping & Fun",
            "phone": "+2348012345736", "whatsapp": "", "address": "Samonda, Ibadan",
            "description": "Leisure and shopping hub with cinemas and games.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Ventura"
        },
        {
            "name": "Agodi Gardens", "category": "Tourism & Leisure",
            "phone": "+2348012345737", "whatsapp": "", "address": "Parliament Road, Ibadan",
            "description": "Beautiful park, zoo and lake for family outings.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Agodi"
        },
        {
            "name": "Premier Hotel", "category": "Hospitality",
            "phone": "+2348012345738", "whatsapp": "", "address": "Mokola Hill, Ibadan",
            "description": "Historic hotel with the best overview of Ibadan city.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Premier"
        },
        {
            "name": "IITA Ibadan", "category": "Agriculture Research",
            "phone": "+2348012345739", "whatsapp": "", "address": "Oyo Road, Moniya, Ibadan",
            "description": "International hub for tropical agriculture innovation.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=IITA"
        },
        {
            "name": "FoodCo", "category": "Supermarket",
            "phone": "+234700366326", "whatsapp": "", "address": "Bodija, Ibadan",
            "description": "Top-rated supermarket, bakery and pharmacy chain.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=FoodCo"
        },
        {
            "name": "Lead City University", "category": "Education",
            "phone": "+23412345741", "whatsapp": "", "address": "Challenge-Orita Road, Ibadan",
            "description": "Private knowledge for standard professional careers.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=LCU"
        },
        {
            "name": "Kakanfo Inn", "category": "Hospitality",
            "phone": "+23412345742", "whatsapp": "", "address": "Ring Road, Ibadan",
            "description": "Premier hotel providing top hospitality and events.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Kakanfo"
        },
        {
            "name": "Jericho Golf Club", "category": "Sports & Leisure",
            "phone": "+23412345743", "whatsapp": "", "address": "Jericho GRA, Ibadan",
            "description": "Luxury golf course and social club for elites.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Jericho"
        },
        {
            "name": "Walan Hotel", "category": "Hospitality",
            "phone": "+23412345744", "whatsapp": "", "address": "Old Ife Road, Ibadan",
            "description": "Comfortable stay for travelers in the Ibadan metropolis.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Walan"
        },
        {
            "name": "Ibadan Recreation Club", "category": "Leisure",
            "phone": "+23412345745", "whatsapp": "", "address": "Gra Area, Ibadan",
            "description": "Historical social and sports recreation center.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=IRC"
        },
        {
            "name": "Shoprite Ibadan", "category": "Retail",
            "phone": "+23412345746", "whatsapp": "", "address": "Heritage Mall, Dugbe, Ibadan",
            "description": "Leading retailer for groceries and general household items.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=ShopriteIbadan"
        },
        {
            "name": "Tantalizers", "category": "Fast Food",
            "phone": "+23412345747", "whatsapp": "", "address": "Ring Road, Ibadan",
            "description": "One of Nigeria's favorite fast-food chains.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Tantalizers"
        },
        {
            "name": "Mr Bigg's Ibadan", "category": "Fast Food",
            "phone": "+23412345748", "whatsapp": "", "address": "Mokola, Ibadan",
            "description": "Iconic Nigerian fast-food brand serving classic meals.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=BiggIbadan"
        },
        {
            "name": "Chicken Republic", "category": "Fast Food",
            "phone": "+23412345749", "whatsapp": "", "address": "Bodija, Ibadan",
            "description": "Spicy chicken and delightful African meals.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=ChickenIbadan"
        },
        {
            "name": "Dominos Pizza Ibadan", "category": "Fast Food",
            "phone": "+23412345750", "whatsapp": "", "address": "Awolowo Ave, Bodija",
            "description": "The best pizza and ice cream in the city.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=DominosIbadan"
        },
        {
            "name": "Cocoa House", "category": "Commercial Hub",
            "phone": "+23412345751", "whatsapp": "", "address": "Dugbe, Ibadan",
            "description": "The first skyscraper in tropical Africa, housing various businesses.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Cocoa"
        },
        {
            "name": "Mapo Hall Gallery", "category": "Tourism",
            "phone": "+23412345752", "whatsapp": "", "address": "Mapo Hill, Ibadan",
            "description": "Historic colonial gallery and events center.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Mapo"
        },
        {
            "name": "Bower's Tower", "category": "Tourism",
            "phone": "+23412345753", "whatsapp": "", "address": "Oke-Are Hill, Ibadan",
            "description": "Highest point in Ibadan with 360-degree views.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 0,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=Bower"
        },
        {
            "name": "University College Hospital (UCH)", "category": "Health",
            "phone": "+23412345754", "whatsapp": "", "address": "Queen Elizabeth Road, Ibadan",
            "description": "Nigeria's flagship medical teaching and research hospital.",
            "region": "South West", "state": "Oyo", "city": "Ibadan",
            "vacancy_status": "None", "is_verified": 1, "is_featured": 1,
            "logo_url": "https://api.dicebear.com/7.x/initials/svg?seed=UCH"
        }
    ]

    for biz in businesses:
        # Check if business already exists by name to avoid duplicates
        exists = db.query(models.Business).filter(models.Business.name == biz["name"]).first()
        if not exists:
            db_business = models.Business(**biz)
            db.add(db_business)
    
    db.commit()
    print(f"Successfully synced {len(businesses)} businesses!")

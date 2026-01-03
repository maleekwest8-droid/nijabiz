---
title: NijaBiz Local Directory
emoji: 💼
colorFrom: green
colorTo: gray
sdk: docker
license: mit
pinned: false
---

# NijaBiz - Local Business Directory MVP

A simple, functional, and aesthetically pleasing local business directory for Nigerian businesses built with FastAPI and SQLite.

## Features
- List of local businesses.
- Search by name or category.
- Form to submit new businesses.
- One-click Call and WhatsApp buttons.
- Fully responsive design using Tailwind CSS.

## Prerequisites
- Python 3.9+
- pip

## Running Locally

### 1. Set up the environment
```bash
# Clone the repository (if applicable)
# Navigate to the project directory
cd "proj 3"

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the application
```bash
python3 -m uvicorn main:app --reload
```
The app will be available at [http://localhost:8000](http://localhost:8000).

### 3. Test Endpoints manually (curl)
```bash
# Health check
curl http://127.0.0.1:8000/health

# List all businesses
curl http://127.0.0.1:8000/businesses

# Add a business
curl -X POST http://127.0.0.1:8000/businesses \
-H "Content-Type: application/json" \
-d '{"name": "Lagos Tech Hub", "category": "Co-working", "phone": "+2348012345678", "whatsapp": "+2348012345678", "address": "123 Herbert Macaulay Way, Yaba, Lagos", "description": "A vibrant hub for tech enthusiasts and startups in Lagos."}'
```

## Deployment Instructions

## 🚀 Deployment (100% Free Forever)

### Option A: Render + Supabase (Recommended)
- **App**: [Render](https://render.com/)
- **Database**: [Supabase](https://supabase.com/)
- **Pros**: Persistent data, very easy to setup.

### Option B: Koyeb (Great Alternative)
- **Platform**: [Koyeb](https://www.koyeb.com/)
- **Tier**: "Nano" (Free)
- **How**: Deploy via GitHub, use `DATABASE_URL` for persistence.

### Option C: Oracle Cloud (Most Powerful)
- **Platform**: [Oracle Cloud Always Free](https://www.oracle.com/cloud/free/)
- **Specs**: 4 ARM OCPUs, 24GB RAM (Incredible for free).
- **Cons**: Requires a credit card for identity verification and can be hard to sign up.

### Option D: Hugging Face Spaces
- **Platform**: [Hugging Face](https://huggingface.co/spaces)
- **Tier**: CPU Basic (Free)
- **How**: Select "Docker" template, upload your code, and it runs for free forever.

### Option E: Vercel (Fastest Frontend)
- **Platform**: [Vercel](https://vercel.com/)
- **How**: Best if you just want to host the `static/` folder as a frontend and point it to a backend.

---

## 🏗 Comparison Table

| Platform | Ease of Use | Persistence | Best For |
| :--- | :--- | :--- | :--- |
| **Render** | ⭐⭐⭐⭐⭐ | Needs Ext. DB | Beginners |
| **Koyeb** | ⭐⭐⭐⭐ | Needs Ext. DB | Quick Deploys |
| **Supabase** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Databases Only |
| **Oracle** | ⭐ | ⭐⭐⭐⭐⭐ | Large Apps |
| **HuggingFace** | ⭐⭐⭐ | ⭐⭐⭐ | Docker/Python |

---

## 🛠 Project Structure
```text
proj 3/
├── main.py              # FastAPI routes (The Brain)
├── models.py            # Database tables
├── schemas.py           # Data validation
├── database.py          # Connection logic (SQLite or Postgres)
├── requirements.txt     # Needed libraries
├── render.yaml          # Auto-deploy config for Render
├── .env.example         # Example settings
└── static/
    └── index.html       # The Beautiful Frontend
```

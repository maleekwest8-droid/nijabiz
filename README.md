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

### Backend (Render) - RECOMMENDED
1. I have included a `render.yaml` file. When you connect your GitHub repo to Render, it will offer to deploy your "Blueprint".
2. This blueprint automatically creates:
   - A **Web Service** for your FastAPI app.
   - A **PostgreSQL Database** for persistent storage (so your data never disappears!).
3. Render will automatically set the `DATABASE_URL` for you.
4. Just click **"Apply"** on the Render dashboard after connecting your repository.

### Backend (Railway)
1. Link your repo to [Railway](https://railway.app).
2. It will auto-detect the requirements and start command.
3. You can add a **Postgres Plugin** and Railway will automatically inject the `DATABASE_URL` environment variable.

### Frontend (Vercel)
Since this is a FastAPI app serving static files, you can deploy the whole thing as a single service on Render/Railway. If you want to deploy the frontend separately on Vercel:
1. Change `API_URL` in `index.html` to your deployed backend URL.
2. Push the `static/` directory to a repo.
3. Deploy to Vercel as a static site.

## Known Limitations
- SQLite database is file-based and may not persist between redeploys on free hosting (Render free tier).
- No authentication for business submission (MVP constraint).
- Minimal search logic (case-insensitive substring match).

# The Glorious Nje Here Ltd — Learning Project

A practical software-engineering portfolio built while learning to create ERP-style systems for Kenyan and East African SMEs.

## Who I am
[Savio]. I am Motivated beginner learning practical software engineering so I can automate business processes for SMEs in Kenya.

## What I am building
A repository that tracks my learning journey toward a mini-ERP for a distributor (bulk orders, credit vs cash customers, delivery status, and collections).  
Practice shop name: **The Glorious Nje Here Ltd**.

## Current status
- Phase 0 in progress
- Local toolchain working (Git + Python 3.13 + venv + .env)
- First working script: `hello.py` that reads configuration from the environment

## Tech stack (learning path)
- Git + GitHub
- Python 3
- PostgreSQL
- Django
- HTML/CSS + HTMX
- Later: Redis/Celery or Django-Q, n8n, Metabase, M-Pesa Daraja sandbox

## How to run the current code
python hello.py         
# Clone the repo (after it is on GitHub)
git clone <repo-url>
cd glorious-nje-here

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows

# Install dependencies
pip install python-dotenv

# Create your own .env (never commit this file)
echo SHOP_NAME=The Glorious Nje Here Ltd > .env

# Run
python hello.py
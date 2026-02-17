import sys
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load env vars
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

def seed_job011():
    print(f"Connecting to MongoDB...")
    client = MongoClient(MONGO_URI)
    db = client["ats_hiring_db"]
    jobs_collection = db["jobs"]

    # Job Data for JOB011 (Python Developer to match STU018)
    new_job = {
        "job_id": "JOB011",
        "title": "Python Backend Developer",
        "company": "TechScale",
        "location": "Remote",
        "salary_max": 900000,
        "experience_required": 2,
        "required_skills": ["Python", "SQL", "FastAPI", "Docker"],
        "qualification": "B.Tech",
        "jd_text": """
        We are looking for a skilled Python Backend Developer to clear technical debt and build new features.
        
        Responsibilities:
        - Develop and maintain scalable backend services using Python and FastAPI.
        - Optimize SQL queries for performance.
        - Containerize applications using Docker.
        - Collaborate with frontend teams to integrate APIs.
        
        Requirements:
        - Strong proficiency in Python and SQL.
        - Experience with FastAPI or Flask.
        - Knowledge of Docker and CI/CD pipelines.
        """
    }

    # Insert or Update
    result = jobs_collection.update_one(
        {"job_id": "JOB011"},
        {"$set": new_job},
        upsert=True
    )

    if result.upserted_id:
        print(f"✅ Created New Job: JOB011")
    else:
        print(f"✅ Updated Existing Job: JOB011")

if __name__ == "__main__":
    seed_job011()

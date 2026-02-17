import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.mongo_db import db

def seed_data():
    print("Connecting to MongoDB...")
    
    # 1. Insert Student STU012
    student_data = {
        "student_id": "STU012",
        "name": "Test User",
        "education": {
            "qualification": "B.Tech"
        },
        "skills": [
            "ReactJS",
            "NodeJS",
            "MongoDB"
        ],
        "experience_years": 3,
        "preferred_location": "Pune",
        "expected_salary": 800000,
        "resume_text": "Experienced ReactJS and NodeJS developer."
    }
    
    # Upsert (Update if exists, Insert if not)
    res_stu = db.students.update_one(
        {"student_id": "STU012"},
        {"$set": student_data},
        upsert=True
    )
    print(f"Student STU012: {'Updated' if res_stu.modified_count > 0 else 'Inserted/Unchanged'}")

    # 2. Insert Job JOB012
    job_data = {
        "job_id": "JOB012",
        "title": "Full Stack Developer",
        "company": "Tech Corp",
        "location": "Pune",
        "salary_max": 1200000,
        "experience_required": 2,
        "required_skills": [
            "React",
            "Node.js",
            "MongoDB"
        ],
        "qualification": "B.Tech",
        "jd_text": "Looking for a MERN stack developer with experience in React and Node.js."
    }
    
    res_job = db.jobs.update_one(
        {"job_id": "JOB012"},
        {"$set": job_data},
        upsert=True
    )
    print(f"Job JOB012: {'Updated' if res_job.modified_count > 0 else 'Inserted/Unchanged'}")

if __name__ == "__main__":
    seed_data()

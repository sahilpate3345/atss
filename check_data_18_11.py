import sys
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load env vars
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

def check_data():
    print(f"Connecting to MongoDB...")
    client = MongoClient(MONGO_URI)
    db = client["ats_hiring_db"]
    
    # Check Student
    student = db.students.find_one({"student_id": "STU018"})
    if student:
        print(f"✅ Found STU018: {student.get('name')} | Skills: {student.get('skills')}")
    else:
        print(f"❌ STU018 NOT FOUND")

    # Check Job
    job = db.jobs.find_one({"job_id": "JOB011"})
    if job:
        print(f"✅ Found JOB011: {job.get('title')} | Required: {job.get('required_skills')}")
    else:
        print(f"❌ JOB011 NOT FOUND")

if __name__ == "__main__":
    check_data()

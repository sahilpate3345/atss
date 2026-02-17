import json
import os
from pathlib import Path
from backend.mongo_db import db

BASE_DIR = Path(__file__).resolve().parent.parent / "database"

def load_json(filename):
    path = BASE_DIR / filename
    if not path.exists():
        print(f"Warning: {filename} not found at {path}")
        return []
    
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            # Handle specific keys for each file structure
            if "students" in data: return data["students"]
            if "jobs" in data: return data["jobs"]
            if "companies" in data: return data["companies"]
            return data 
        except json.JSONDecodeError:
            print(f"Error decoding {filename}")
            return []

def migrate():
    print("Starting Migration from JSON to MongoDB...")

    # Students
    students = load_json("students.json")
    if students:
        if db.students.count_documents({}) == 0:
            db.students.insert_many(students)
            print(f"Migrated {len(students)} students.")
        else:
            print(f"Skipping students migration: Collection not empty.")

    # Jobs
    jobs = load_json("jobs.json")
    if jobs:
        if db.jobs.count_documents({}) == 0:
            db.jobs.insert_many(jobs)
            print(f"Migrated {len(jobs)} jobs.")
        else:
            print(f"Skipping jobs migration: Collection not empty.")

    # Companies
    companies = load_json("companies.json")
    if companies:
        if db.companies.count_documents({}) == 0:
            db.companies.insert_many(companies)
            print(f"Migrated {len(companies)} companies.")
        else:
            print(f"Skipping companies migration: Collection not empty.")

    print("Migration Check Complete!")

if __name__ == "__main__":
    migrate()

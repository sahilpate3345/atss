
import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv
from collections import Counter

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "ats_hiring_db")

def check_jobs():
    print(f"Connecting to MongoDB: {MONGO_URI} ...")
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    jobs_count = db.jobs.count_documents({})
    print(f"Total Jobs in DB: {jobs_count}")
    
    if jobs_count == 0:
        print("No jobs found.")
        return

    # Fetch all job_ids
    all_jobs = list(db.jobs.find({}, {"job_id": 1, "title": 1, "_id": 0}))
    
    job_ids = [j.get("job_id", "UNKNOWN") for j in all_jobs]
    counts = Counter(job_ids)
    
    duplicates = {jid: count for jid, count in counts.items() if count > 1}
    
    if duplicates:
        print("\n!!! DUPLICATES FOUND !!!")
        for jid, count in duplicates.items():
            print(f" - {jid}: {count} occurrences")
            
        # Detail on duplicates
        print("\nDuplicate Details:")
        for jid in duplicates:
            docs = list(db.jobs.find({"job_id": jid}))
            for i, doc in enumerate(docs):
                print(f"  {i+1}. _id: {doc['_id']} | Title: {doc.get('title')}")
    else:
        print("\nNo duplicates found based on 'job_id'.")
        print("Job IDs found:")
        for jid in counts:
            print(f" - {jid}")

if __name__ == "__main__":
    check_jobs()

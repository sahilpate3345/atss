import sys
import os
import json

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.json_db import read_db
from backend.ats_matcher import ats_score
from backend.interview_engine import generate_questions

def debug_interview(student_id, job_id):
    print(f"Debugging Interview for Student: {student_id}, Job: {job_id}")
    
    # 1. Load Data
    data_students = read_db("students.json")
    students = data_students.get("students", [])
    student = next((s for s in students if s["student_id"] == student_id), None)
    
    data_jobs = read_db("jobs.json")
    jobs = data_jobs.get("jobs", [])
    job = next((j for j in jobs if j["job_id"] == job_id), None)
    
    if not student:
        print("❌ Student NOT FOUND")
        return
    if not job:
        print("❌ Job NOT FOUND")
        return
        
    print(f"✅ Found Student: {student['name']}")
    print(f"✅ Found Job: {job['title']}")
    
    # 2. Generate Questions
    print("\n❓ Attempting to generate questions (Real LLM Test)...")
    try:
        questions = generate_questions(job, student)
        print(f"✅ Questions Generated: {len(questions)}")
        for i, q in enumerate(questions, 1):
            print(f"  {i}. {q}")
            
        if len(questions) < 3:
             print("⚠️ Warning: Too few questions generated.")
        else:
             print("✅ Question count is sufficient.")
             
    except Exception as e:
        print(f"❌ Error generating questions: {e}")

if __name__ == "__main__":
    debug_interview("STU018", "JOB011")

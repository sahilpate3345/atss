from fastapi import FastAPI
from backend.json_db import read_db
from backend.ats_matcher import ats_score
from backend.interview_engine import generate_questions
from backend.expected_answers import generate_expected_answers
from backend.evaluation_engine import evaluate_interview

app = FastAPI(title="AI ATS Hiring System")


@app.get("/")
def home():
    return {"message": "ATS Backend Running"}


# ---------------- JOB RECOMMENDATION ----------------
@app.get("/recommend/{student_id}")
def recommend_jobs(student_id: str):

    data = read_db("students.json")
    students = data.get("students", [])
    
    data_jobs = read_db("jobs.json")
    jobs = data_jobs.get("jobs", [])

    student = next((s for s in students if s["student_id"] == student_id), None)
    if not student:
        return {"error": "Student not found"}

    results = []
    for job in jobs:
        score = ats_score(student, job)
        if score > 20:
            results.append({
                "job_id": job["job_id"],
                "title": job["title"],
                "score": score
            })

    return sorted(results, key=lambda x: x["score"], reverse=True)


# ---------------- START INTERVIEW ----------------
@app.get("/start_interview/{student_id}/{job_id}")
def start_interview(student_id: str, job_id: str):

    data = read_db("students.json")
    students = data.get("students", [])
    
    data_jobs = read_db("jobs.json")
    jobs = data_jobs.get("jobs", [])

    student = next((s for s in students if s["student_id"] == student_id), None)
    job = next((j for j in jobs if j["job_id"] == job_id), None)
    
    if not student or not job:
         return {"error": "Student or Job not found"}

    questions = generate_questions(job, student)
    expected = generate_expected_answers(questions, job)

    return {"questions": questions, "expected_answers": expected}


# ---------------- SUBMIT INTERVIEW ----------------
@app.post("/submit_interview")
def submit_interview(data: dict):

    score = evaluate_interview(data["answers"], data["expected"])
    status = "Shortlisted" if score >= 5 else "Rejected"

    return {"interview_score": score, "status": status}

from backend.skill_normalizer import normalizer
from backend.embedding_engine import get_similarity

def skill_match(student_skills, job_skills):
    if not job_skills:
        return 0
    
    # Normalize skills using the dictionary map
    # This fixes "ReactJS" vs "React" issues
    s_norm = set(normalizer.normalize(student_skills))
    j_norm = set(normalizer.normalize(job_skills))
    
    # Calculate intersection on normalized sets
    # We use Set Intersection instead of TF-IDF/Cosine Similarity here because:
    # 1. Cosine Similarity penalizes candidates with extra skills (Vector length normalization).
    # 2. We want to measure "Coverage" (How many required skills does the candidate have?), not "Text Similarity".
    if not j_norm:
        return 0
        
    match_count = len(s_norm & j_norm)
    return match_count / len(j_norm)

def ats_score(student, job):

    skill_score = skill_match(student.get("skills", []), job.get("required_skills", [])) * 40
    
    # Qualification (Case insensitive)
    student_qual = student.get("education", {}).get("qualification", "").lower()
    job_qual = job.get("qualification", "").lower()
    qualification = 15 if student_qual == job_qual else 0
    
    # Experience
    exp = 15 if student.get("experience_years", 0) >= job.get("experience_required", 0) else 5
    
    # Location
    stud_loc = student.get("preferred_location", "").lower()
    job_loc = job.get("location", "").lower()
    location = 10 if stud_loc == job_loc else 0
    
    # Salary
    salary = 10 if student.get("expected_salary", 99999999) <= job.get("salary_max", 0) else 5
    
    # Semantic
    semantic = get_similarity(student.get("resume_text", ""), job.get("jd_text", "")) * 10

    # Total Score
    return round(skill_score + qualification + exp + location + salary + semantic, 2)

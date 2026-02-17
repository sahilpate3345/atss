from backend.llm_groq import ask_llm

import json

def generate_questions(job, student):
    jd_text = job.get('jd_text', '')
    title = job.get('title', 'Generic Role')
    skills = job.get('required_skills', [])
    student_skills = student.get('skills', [])
    exp = student.get('experience_years', 0)

    prompt = f"""
    You are an expert technical interviewer. Generate 10 technical interview questions for a candidate applying for the role of {title}.
    
    Job Description:
    {jd_text}
    
    Required Skills: {skills}
    Candidate Skills: {student_skills}
    Experience Level: {exp} years
    
    Instructions:
    1. Questions must be relevant to the Job Description and Required Skills.
    2. Assess the candidate's depth of knowledge appropriate for {exp} years of experience.
    3. Return the output as a strictly valid JSON list of strings. Do not add any markdown formatting or introductory text.
    4. Example format: ["Question 1", "Question 2", ...]
    """
    
    response_text = ask_llm(prompt)
    
    # DEBUG LOGGING
    try:
        with open("backend/debug.log", "a", encoding="utf-8") as f:
            f.write(f"\n--- NEW REQUEST ---\nRole: {title}\n")
            f.write(f"Raw LLM Response: {response_text}\n")
    except Exception as e:
        print(f"Logging failed: {e}")

    # Attempt to parse JSON
    try:
        # Clean up potential markdown code blocks if the LLM adds them
        clean_text = response_text.replace("```json", "").replace("```", "").strip()
        questions = json.loads(clean_text)
        if isinstance(questions, list):
             # Validate content isn't just empty strings
             questions = [q for q in questions if isinstance(q, str) and len(q.strip()) > 5]
             
             if len(questions) >= 3:
                 with open("backend/debug.log", "a", encoding="utf-8") as f:
                     f.write(f"Parsed JSON Successfully: {questions[:2]}...\n")
                 return questions[:10]
    except json.JSONDecodeError:
        # Fallback to line splitting if JSON fails
        pass
        
    # Fallback/Original parsing if JSON fails or structure is wrong
    questions = [q.strip() for q in response_text.split("\n") if q.strip()]
    
    # Remove numbering "1. ", "2. " etc if present in fallback headers
    cleaned_questions = []
    for q in questions:
        # Simple heuristic to remove leading numbers
        parts = q.split(".", 1)
        if len(parts) > 1 and parts[0].strip().isdigit():
            cleaned_questions.append(parts[1].strip())
        else:
            cleaned_questions.append(q)
            
    # VALIDATION: Ensure we actually have questions
    if not cleaned_questions or len(cleaned_questions) < 3:
        # Fallback if LLM failed completely or returned garbage
        print(f"⚠️ LLM failed to generate valid questions. Using Fallback.")
        with open("backend/debug.log", "a", encoding="utf-8") as f:
            f.write(f"⚠️ Triggering FALLBACK. Cleaned questions count: {len(cleaned_questions)}\n")
            
        return [
            "[System Note: API Unavailable - Using Backup Technical Questions]",
            f"Technically describe your experience with {title} and {skills[0] if skills else 'relevant technologies'}.",
            f"What are the core differences between {skills[0] if skills else 'Option A'} and {skills[1] if len(skills)>1 else 'Option B'}?",
            f"Walk me through a production issue you solved involving {skills[-1] if skills else 'debugging'}.",
            "Explain the concept of ACID properties in databases.",
            "How do you approach optimizing a slow API endpoint?"
        ]

    return cleaned_questions[:10]

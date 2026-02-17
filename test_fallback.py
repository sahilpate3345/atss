import sys
import os
from unittest.mock import patch, MagicMock

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.interview_engine import generate_questions

def test_fallback():
    print("\n--- Testing Fallback Mechanism ---")
    
    # Mock Data
    job = {
        "title": "Chaos Engineer",
        "jd_text": "Break things on purpose.",
        "required_skills": ["Python", "Chaos Monkey"]
    }
    student = {
        "skills": ["Python"],
        "experience_years": 5
    }

    # 1. Test Empty Response from LLM
    print("\n[Scenario 1] LLM returns empty string")
    with patch("backend.interview_engine.ask_llm", return_value=""):
        questions = generate_questions(job, student)
        print(f"Questions Returned: {len(questions)}")
        for q in questions:
            print(f"- {q}")
            
        if len(questions) == 5 and "Describe your experience" in questions[0]:
            print("✅ Fallback Triggered Successfully!")
        else:
            print("❌ Fallback Failed.")

    # 2. Test Garbage Response
    print("\n[Scenario 2] LLM returns garbage JSON")
    with patch("backend.interview_engine.ask_llm", return_value="{'wrong': 'format'}"):
        questions = generate_questions(job, student)
        print(f"Questions Returned: {len(questions)}")
        # Expect fallback because it's not a list
        if len(questions) == 5:
             print("✅ Fallback Triggered (Garbage JSON)!")
        else:
             print(f"❌ Fallback Failed. Got: {questions}")

    # 3. Test API Error Message
    print("\n[Scenario 3] LLM returns API Error message")
    with patch("backend.interview_engine.ask_llm", return_value="Error: API Limit Exceeded"):
        questions = generate_questions(job, student)
        if len(questions) == 5:
             print("✅ Fallback Triggered (API Error)!")
        else:
             print(f"❌ Fallback Failed. Got: {questions}")

if __name__ == "__main__":
    test_fallback()

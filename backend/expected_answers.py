from backend.llm_groq import ask_llm

def generate_expected_answers(questions, job):
    answers = []
    for q in questions:
        prompt = f"You are an expert {job.get('title', 'professional')}. Give short ideal answer: {q}"
        answers.append(ask_llm(prompt))
    return answers

from backend.embedding_engine import get_similarity

def score_answer(student_ans, expected_ans):
    sim = get_similarity(student_ans, expected_ans)

    if sim > 0.80:
        return 1
    elif sim > 0.60:
        return 0.7
    elif sim > 0.40:
        return 0.4
    else:
        return 0

def evaluate_interview(student_answers, expected_answers):
    total = 0
    for s, e in zip(student_answers, expected_answers):
        total += score_answer(s, e)
    return round(total, 2)

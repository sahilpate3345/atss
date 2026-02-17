try:
    from models.embedding_models import similarity
except ImportError:
    # Fallback if running from backend dir
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from models.embedding_models import similarity

def get_similarity(text1, text2):
    return similarity(text1, text2)

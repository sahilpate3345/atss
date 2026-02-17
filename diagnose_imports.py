import sys
import os
from pathlib import Path

# Simulate adding root to path like register.py does
root_path = Path(__file__).resolve().parent
sys.path.append(str(root_path))

print(f"sys.path: {sys.path}")

try:
    print("Attempting to import backend.mongo_db...")
    from backend.mongo_db import db
    print("Successfully imported backend.mongo_db")
except Exception as e:
    print(f"Failed to import backend.mongo_db: {e}")

try:
    print("Attempting to import frontend_streamlit.register...")
    import frontend_streamlit.register
    print("Successfully imported frontend_streamlit.register")
except Exception as e:
    print(f"Failed to import frontend_streamlit.register: {e}")

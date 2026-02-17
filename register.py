# Add project root to sys.path to allow importing backend modules
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.mongo_db import db
import streamlit as st

def app():
    st.header("Student Registration")

    name = st.text_input("Full Name")
    qualification = st.text_input("Qualification")
    skills = st.text_area("Skills (comma separated)")
    experience = st.number_input("Experience (years)", 0, 20)
    location = st.text_input("Preferred Location")
    salary = st.number_input("Expected Salary", 0)
    resume = st.text_area("Resume Summary")

    if st.button("Register"):

        if not name:
            st.warning("Please enter name")
            return

        # Database Insertion
        try:
            # from backend.mongo_db import db # Imported at top level
            
            # Generate ID (fetch count from DB)
            count = db.students.count_documents({})
            student_id = f"STU{count+1:03d}"

            new_student = {
                "student_id": student_id,
                "name": name,
                "education": {"qualification": qualification},
                "skills": [s.strip() for s in skills.split(",") if s.strip()],
                "experience_years": experience,
                "preferred_location": location,
                "expected_salary": salary,
                "resume_text": resume
            }

            db.students.insert_one(new_student)
            st.success(f"Registered Successfully! Your ID: {student_id}")

        except Exception as e:
            st.error(f"Error connecting to database: {e}")

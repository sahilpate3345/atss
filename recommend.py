import streamlit as st
import requests

def app():
    st.header("Job Recommendations")

    student_id = st.text_input("Enter Student ID")

    if st.button("Get Recommendations"):

        if not student_id:
            st.warning("Enter student ID")
            return

        try:
            res = requests.get(f"http://127.0.0.1:8080/recommend/{student_id}")
            
            if res.status_code != 200:
                st.error(f"Error: {res.json()}")
                return
                
            jobs = res.json()

            if not jobs:
                st.warning("No matching jobs found")
            else:
                for job in jobs:
                    st.subheader(job.get("title", "Unknown Job"))
                    st.write(f"Match Score: {job.get('score', 0)}")
                    st.write("---")

        except requests.exceptions.ConnectionError:
            st.error("Backend server not running. Please start the backend.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

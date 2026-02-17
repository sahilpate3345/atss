import streamlit as st
import requests

def app():
    st.header("AI Interview")

    # Use session state to persist data across reruns
    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False
        st.session_state.questions = []
        st.session_state.expected = []

    student_id = st.text_input("Student ID")
    job_id = st.text_input("Job ID")

    if st.button("Start Interview"):
        if not student_id or not job_id:
            st.warning("Enter student ID and job ID")
            return

        try:
            res = requests.get(f"http://127.0.0.1:8080/start_interview/{student_id}/{job_id}")
            if res.status_code == 200:
                data = res.json()
                st.session_state.questions = data.get("questions", [])
                st.session_state.expected = data.get("expected_answers", [])
                st.session_state.interview_started = True
                st.rerun() # Rerun to show questions immediately
            else:
                 st.error(f"Backend Error: {res.text}")
        except requests.exceptions.ConnectionError:
            st.error("Backend server not running.")

    if st.session_state.interview_started:
        st.subheader("Answer all questions:")
        
        answers = []
        for i, q in enumerate(st.session_state.questions):
            st.write(f"Q{i+1}: {q}")
            # Use unique keys for each text input
            ans = st.text_input(f"Answer {i+1}", key=f"ans_{i}")
            answers.append(ans)

        if st.button("Submit Interview"):
            try:
                result = requests.post(
                    "http://127.0.0.1:8080/submit_interview",
                    json={"answers": answers, "expected": st.session_state.expected}
                )
                if result.status_code == 200:
                    output = result.json()
                    st.success(f"Score: {output.get('interview_score', 0)}")
                    st.info(f"Status: {output.get('status', 'Unknown')}")
                    
                    # Optional: Reset state after submission
                    # st.session_state.interview_started = False
                else:
                    st.error("Submission failed")
            except requests.exceptions.ConnectionError:
                st.error("Backend server not running.")

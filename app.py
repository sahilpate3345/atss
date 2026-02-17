import streamlit as st

# Import the page modules
# (assuming files are in the same directory or python path is set correctly)
try:
    import register
    import recommend
    import interview
except ImportError:
    # If running from root, streamlit adds root to path, so direct import depends on where files are
    # This try-except block handles potential import issues if not running from root
    import frontend_streamlit.register as register
    import frontend_streamlit.recommend as recommend
    import frontend_streamlit.interview as interview

st.set_page_config(page_title="AI ATS Hiring System", layout="wide")

st.title("AI ATS Hiring System")

# Function-based navigation prevents import execution issues
PAGES = {
    "Register": register,
    "Job Recommendations": recommend,
    "Interview": interview
}

selection = st.sidebar.radio("Navigation", list(PAGES.keys()))

page = PAGES[selection]
page.app()

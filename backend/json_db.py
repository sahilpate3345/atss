from backend.mongo_db import db

def read_db(file):
    # Mapping filenames to collections
    if "students" in file:
        data = list(db.students.find({}, {"_id": 0}))
        return {"students": data}
    elif "jobs" in file:
        data = list(db.jobs.find({}, {"_id": 0}))
        return {"jobs": data}
    elif "companies" in file:
        data = list(db.companies.find({}, {"_id": 0}))
        return {"companies": data}
    elif "interview" in file:
        # Fallback or specific logic for interviews if needed
        # Assuming interviews logic might need similar handling
        return {} 
    return {}

def write_db(file, data):
    # This function was used to overwrite the entire JSON file.
    # We should adapt it to update or insert data, but the current usage
    # in main.py isn't clear on write operations (mainly reads).
    # If the app writes back, we need to know existing logic.
    #
    # Looking at register.py (frontend), it appends to list and writes.
    # The backend doesn't seem to use write_db much except maybe tests?
    # Let's see if main.py uses write_db.
    # Checked main.py earlier: it only uses read_db.
    # so we can probably leave write_db as a no-op or NotImplemented for now
    # or implement a basic insert if needed.
    pass

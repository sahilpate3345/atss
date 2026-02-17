import requests
import sys

try:
    print("Testing Backend Connection...")
    r = requests.get("http://127.0.0.1:8080/")
    print(f"Root Endpoint: {r.status_code}")
    print(f"Response: {r.json()}")

    print("\nTesting Job Recommendation...")
    r = requests.get("http://127.0.0.1:8080/recommend/STU001")
    print(f"Recommend Endpoint: {r.status_code}")
    # print(f"Response: {r.json()}") # Commented out to avoid clutter

    if r.status_code == 200:
        print("\nSUCCESS: Backend is running and responding!")
    else:
        print("\nWARNING: Backend responded with error.")

except Exception as e:
    print(f"\nERROR: Could not connect to backend. Is it running? {e}")

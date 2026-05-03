import requests

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Health Check: {response.status_code} - {response.json()}")
    except requests.exceptions.ConnectionError:
        print("Error: Is the FastAPI server running? (Try: uvicorn app.main:app)")

def test_pdf_upload(file_path):
    print(f"\nTesting PDF: {file_path}...")
    try:
        with open(file_path, "rb") as f:
            files = {"pdf": (file_path, f, "application/pdf")}
            response = requests.post(f"{BASE_URL}/api/upload-pdf", files=files)

        if response.status_code == 200:
            print("Success!")
            data = response.json()
            print(f"Summary Snippet: {data.get('summary')[:150]}...")
        else:
            print(f"Server returned {response.status_code}: {response.text}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def test_audio_upload(file_path):
    print(f"\nTesting Audio: {file_path}...")
    try:
        with open(file_path, "rb") as f:
            files = {"audio": (file_path, f, "audio/mpeg")}
            response = requests.post(f"{BASE_URL}/api/upload-audio", files=files)

        if response.status_code == 200:
            print("Success!")
            data = response.json()
            print(f"Questions Snippet: {data.get('questions')[:150]}...")
        else:
            print(f"Server returned {response.status_code}: {response.text}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    test_health()

import requests

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    response = requests.get(f"{BASE_URL}/")
    print(f"Health Check: {response.status_code} - {response.json()}")

def test_pdf_upload(file_path):
    print(f"\nTesting PDF Upload: {file_path}...")
    with open(file_path, "rb") as f:
        files = {"pdf": f}
        response = requests.post(f"{BASE_URL}/api/upload-pdf", files=files)
    
    if response.status_code == 200:
        print("✅ Success!")
        print(f"Summary: {response.json().get('summary')[:100]}...")
    else:
        print(f"❌ Failed: {response.text}")

def test_audio_upload(file_path):
    print(f"\nTesting Audio Upload: {file_path}...")
    with open(file_path, "rb") as f:
        files = {"audio": f}
        response = requests.post(f"{BASE_URL}/api/upload-audio", files=files)
    
    if response.status_code == 200:
        print("✅ Success!")
        print(f"Questions: {response.json().get('questions')[:100]}...")
    else:
        print(f"❌ Failed: {response.text}")

if __name__ == "__main__":
    # 1. Check if server is up
    test_health()
    
    # 2. Test PDF (Ensure you have a file named 'test.pdf' in your folder)
    # test_pdf_upload("test.pdf")
    
    # 3. Test Audio (Ensure you have a file named 'test.mp3' in your folder)
    # test_audio_upload("test.mp3")

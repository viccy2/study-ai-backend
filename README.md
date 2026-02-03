# 📚 StudyAI: AI-Powered Academic application

A high-throughput FastAPI backend that leverages **OpenAI GPT-4o** and **Whisper-1** to transform unstructured academic data (PDFs and Audio) into structured study materials.

---

```text
study-ai-backend/
├── app/
│   ├── main.py              # Entry point: FastAPI initialization & Routes
│   ├── services/            # Business Logic Layer
│   │   ├── __init__.py      # Package hoisting for clean imports
│   │   ├── openai_service.py # LLM orchestration (Summaries/Quizzes)
│   │   ├── pdf_service.py    # Document parsing logic (PyMuPDF)
│   │   └── audio_service.py  # Transcription logic (Whisper)
├── .env.example             # Template for API keys
├── .gitignore               # Excludes secrets and junk files
├── Dockerfile               # Production containerization
├── requirements.txt         # Dependency manifest
└── test_api.py              # Automated integration test script


## 🛠️ Setup
1. `pip install -r requirements.txt`
2. Create `.env` with `OPENAI_API_KEY=your_key`
3. Run: `python -m uvicorn app.main:app --reload`

## 🧪 Testing
* **Interactive UI**: Visit `http://127.0.0.1:8000/`
* **Script**: Run `python test_api.py`

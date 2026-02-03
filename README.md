# StudyAI Backend 🚀

An AI-powered service that transforms PDFs and Audio recordings into structured study material (summaries and practice quizzes) using **FastAPI** and **OpenAI (GPT-4o & Whisper)**.



## ✨ Key Features
- **PDF Extraction**: Automated text parsing from documents using PyMuPDF.
- **Audio Transcription**: Speech-to-text processing for lectures via OpenAI Whisper.
- **AI Synthesis**: Intelligent summarization and practice question generation.
- **Asynchronous Design**: Built with FastAPI for high-performance I/O.

## 🛠️ Tech Stack
- **Framework**: FastAPI (Python)
- **AI/ML**: OpenAI GPT-3.5-Turbo, Whisper-1
- **File Processing**: PyMuPDF (fitz)
- **DevOps**: Docker, Environment-based configuration

## 🚀 Getting Started

### 1. Clone & Setup
```bash
git clone
cd study-ai-backend
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
pip install -r requirements.txt

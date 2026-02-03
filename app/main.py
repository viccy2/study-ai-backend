import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Import our logic from the service files we're about to create
from app.services.pdf_service import extract_text_from_pdf
from app.services.audio_service import transcribe_audio
from app.services.openai_service import generate_study_material

load_dotenv()

app = FastAPI(title="StudyAI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    try:
        text = await extract_text_from_pdf(file)
        result = await generate_study_material(text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/process-audio")
async def process_audio(file: UploadFile = File(...)):
    try:
        transcript = await transcribe_audio(file)
        result = await generate_study_material(transcript)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

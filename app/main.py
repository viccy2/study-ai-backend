import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Clean imports from our service package
from app.services import extract_text_from_pdf, transcribe_audio, generate_study_material

load_dotenv()

app = FastAPI(title="StudyAI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return {"status": "online", "message": "StudyAI Backend is running"}

@app.post("/api/upload-pdf")
async def process_pdf(pdf: UploadFile = File(...)):
    try:
        text = await extract_text_from_pdf(pdf)
        return await generate_study_material(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF Processing Error: {str(e)}")

@app.post("/api/upload-audio")
async def process_audio(audio: UploadFile = File(...)):
    try:
        transcript = await transcribe_audio(audio)
        return await generate_study_material(transcript)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio Processing Error: {str(e)}")

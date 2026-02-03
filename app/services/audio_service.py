import openai
import tempfile
import os
from fastapi import UploadFile

async def transcribe_audio(file: UploadFile) -> str:
    client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    suffix = os.path.splitext(file.filename)[1]
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        with open(tmp_path, "rb") as audio_file:
            transcript = await client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        return transcript.text
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

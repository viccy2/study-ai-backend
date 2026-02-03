import openai
import os

async def generate_study_material(text: str):
    # Truncate to stay within token limits
    context = text[:4000]
    
    # Using the modern OpenAI client (Async)
    client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    summary_prompt = f"Summarize this: {context}"
    quiz_prompt = f"Generate 5 questions with answers from this: {context}"
    
    # In a real FAANG setup, you'd run these in parallel with asyncio.gather
    summary = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": summary_prompt}]
    )
    
    questions = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": quiz_prompt}]
    )
    
    return {
        "summary": summary.choices[0].message.content,
        "questions": questions.choices[0].message.content
    }

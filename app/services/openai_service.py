import openai
import os
import asyncio

async def generate_study_material(text: str):
    client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    context = text[:4000] # Safe token limit for GPT-3.5
    
    # Running tasks in parallel to save time
    summary_task = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Summarize this text for a student."},
                  {"role": "user", "content": context}]
    )
    
    quiz_task = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Generate 5 practice questions with answers."},
                  {"role": "user", "content": context}]
    )

    summary_res, quiz_res = await asyncio.gather(summary_task, quiz_task)

    return {
        "summary": summary_res.choices[0].message.content,
        "questions": quiz_res.choices[0].message.content
    }

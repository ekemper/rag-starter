import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(query, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""You are an assistant helping answer questions using provided information.
    
Context:
{context}

Question:
{query}

Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

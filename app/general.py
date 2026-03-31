import pandas as pd
from pathlib import Path
from  dotenv import  load_dotenv
from groq import Groq
import os
import re
from chromadb.utils import embedding_functions

from sympy.physics.units import temperature

load_dotenv()

client_general = Groq()
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name='sentence-transformers/all-MiniLM-L6-v2')

general_prompt = '''
You are a friendly and helpful AI assistant for an e-commerce chatbot.

Your job:
- Respond to general conversation (greetings, small talk, simple questions)
- Keep answers short, clear, and polite
- If the user asks about products, pricing, or orders, guide them politely
- Do NOT make up product details or prices
- If unsure, say "I'm not sure, but I can help you find that"

Tone:
- Friendly
- Simple English
- Human-like

Examples:
User: Hi
Assistant: Hello! How can I help you today?

User: How are you?
Assistant: I'm doing great! How can I assist you?

User: Tell me a joke
Assistant: Sure! Why did the computer go to the doctor? Because it caught a virus 😄

'''


def handle_text(text):
    try:
        response = client_general.chat.completions.create(
            model = os.environ["GROQ_MODEL"],
            messages =[
                {
                    "role" : "system",
                    "content" : general_prompt
                },
                {
                    "role":"user",
                    "content":text
                }

            ],
            temperature=0.7,
            max_tokens = 100
        )

        return response.choices[0].message.content

    except Exception as e :
        return f"Error :{str(e)}"

if __name__ == "__main__":
    text = ("Hii , how was your day")
    response = handle_text(text)
    print (response)









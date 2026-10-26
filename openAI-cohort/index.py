from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Write a short poem about The story of a goat, rephrase it : Ek bakri ka khud ka kahani."
        }
    ]
)

print(response.choices[0].message.content)
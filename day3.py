from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "What is the best way to distribute an indie product?"}]
)
print(response.choices[0].message.content)

prompt = """
You are a distribution strategist for indie founders.
Given a product description, suggest 3 specific communities to post in.
Be specific - give actual subreddit names, Discord servers or Facebook groups.

Product: A Notion template for student productivity
Audience: College students
Budget: Zero

Respond with only a numbered list
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)
print(response.choices[0].message.content)
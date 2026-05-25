from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key = os.environ.get("GROQ_API_KEY"))

product = "FirstUsers - an AI tool that gives founders a distribution plan"
audience = "indie hackers and solo founders"
budget = "zero"

prompt = f"""
Return ONLY a JSON object with no extra text, no markdown, no backticks.

Given this product:
- Product: {product}
- Audience: {audience}
- Budget: {budget}

Return this exact structure:
{{
  "channels": [
    {{
      "name": "channel name",
      "type": "subreddit/discord/facebook/twitter",
      "why": "one sentence why this fits",
      "message_template": "ready to post message for this channel"
    }}
  ],
  "week1_actions": ["action 1", "action 2", "action 3"]
}}

Give 3 channels. Be specific with the real community names.
"""
response = client.chat.completions.create(
    model= "llama-3.3-70b-versatile",
    messages=[
        {"role" : "system", "content":"You are a growth strategist for indie founders."},
        {"role": "user", "content": prompt}
    ]
)
raw = response.choices[0].message.content

try:
    result = json.loads(raw)
    print(json.dumps(result, indent=2))
except json.JSONDecodeError:
    print("Model didn't return clean JSON, raw response:")
    print(raw)
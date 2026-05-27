from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key= os.environ.get("GROQ_API_KEY"))

product = "DistroAI - ai tool that gives indie founders the distribution plan"
audience = "Indie founder and hackers"
budget = "zero"


prompt_v1 = f"""
Think step by step:
1. First identify what type of product this is
2. Then identify where its ideal users hang out online
3. Then suggest the 3 best specific communities

Product: {product}
Audience: {audience}
Budget: {budget}

Respond with only a numbered list of 3 communities with one sentence each explaining why.
"""

# ---- PROMPT VERSION 2 — Few Shot ----
prompt_v2 = f"""
Here is an example of good output:
Product: Figma plugin for designers
Best community: r/graphic_design — 800k designers, very active, welcomes tool launches

Now do the same for:
Product: {product}
Audience: {audience}
Budget: {budget}

Give 3 communities. Be specific — real subreddit names, Discord servers, or Facebook groups.
"""

# ---- PROMPT VERSION 3 — Negative Prompting ----
prompt_v3 = f"""
Do NOT suggest generic communities like r/entrepreneur or r/startups.
Do NOT give vague advice like "post on social media".
Instead give SPECIFIC niche communities where this exact audience is active.

Product: {product}
Audience: {audience}
Budget: {budget}

Give 3 highly specific communities with exactly one sentence on why each fits.

"""
prompts = [
    ("chain of thought", prompt_v1),
    ("few shot", prompt_v2),
    ("negative prompting", prompt_v3)
]

for name, prompt in prompts:
    print(f"\n{'='*50}")
    print(f"version:{name}")
    print('='*50)

    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages= [
            {"role": "system", "content": "you are a growth strategist for indie founders"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    print(response.choices[0].message.content)
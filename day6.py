from groq import Groq
import os
import json
from dotenv import load_dotenv
from prompts import get_distribution_prompt

load_dotenv()
client = Groq(api_key= os.environ.get("GROQ_API_KEY"))

def get_distribution_plan(product,audience,budget):
    prompt = get_distribution_prompt(product,audience,budget)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages= [
            {"role":"system", "content":"you are a growth strategist for indie founders. Always respind in valid json only. No extra text"},
            {"role":"user", "content":prompt}
        ],
        temperature=0.7
    )
    raw = response.choices[0].message.content

    try:
        result = json.loads(raw)
        return result
    except json.JSONDecodeError:
        return {"raw": raw,"error": "could not parse as json"}
    

def save_plan(plan, filename = "my_distribution_plan.json"):
    with open(filename,"w") as f:
        json.dump(plan,f, indent=2)
        print(f"\n plan saved to {filename}")

def display_plan(plan):
    if "error" in plan:
        print("\n Got a response but not clear json:")
        print(plan["raw"])
        return
    
    print("\n YOUR DISTROAI DISTRIBUTION PLAN")
    print("="*50)

    if "channels" in plan:
        for i, channel in enumerate(plan["channels"], 1):
            print(f"\n Channel {i}: {channel.get('name', 'N/A')}")
            print(f"Why: {channel.get('why', 'N/A')}")
            print(f"message:{channel.get('message_template','N/A')}")

    if "week1_actions" in plan:
        print("\n Week 1 actions:")
        for action in plan["week1_actions"]:
            print(f"{action}")

if __name__ == "__main__":
    print("Welcome to DistroAI - AI Distribution Planner")
    print("="*50)

    product = input("\n What did you build")
    audience = input("\n Who is it for?")
    budget = input("Budget(zero/small/decent)?")

    print("\n Generating your distribution plan....\n")

    plan = get_distribution_plan(product, audience, budget)
    display_plan(plan)
    save_plan(plan)
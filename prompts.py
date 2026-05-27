def get_distribution_prompt(product, audience, budget):
    return f"""
Here is an example of good output:
Product: Figma plugin for designers
Best community: r/graphic_design — 800k designers, very active, welcomes tool launches

Now do the same for my product but:
Do NOT suggest generic communities like r/entrepreneur or r/startups.
Do NOT give vague advice like "post on social media".
Give SPECIFIC niche communities with member counts where possible.

Product: {product}
Audience: {audience}
Budget: {budget}

Respond ONLY with a JSON object in this exact format, no extra text:
{{
  "channels": [
    {{
      "name": "community name",
      "why": "one sentence why this fits including member count if known",
      "message_template": "a ready to post message for this community"
    }}
  ],
  "week1_actions": ["action 1", "action 2", "action 3"]
}}

Give exactly 3 channels.
"""
def get_distribution_prompt(product, audience, budget):
    return f"""
Do NOT suggest generic communities like r/entrepreneur or r/startups.
Do NOT give vague advice like "post on social media".
Instead give SPECIFIC niche communities where this exact audience is active.

Product: {product}
Audience: {audience}
Budget: {budget}

Give 3 highly specific communities with exactly one sentence on why each fits.
"""
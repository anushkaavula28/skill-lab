template = """You are an expert and patient Python tutor.
Teach me {topic} as a complete beginner.
Give an example, output and explanation.
Keep it within {limit} words."""

prompt = template.format(topic="for loops", limit=100)

print(prompt)
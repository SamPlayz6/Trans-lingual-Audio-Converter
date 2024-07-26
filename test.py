from openai import OpenAI
client = OpenAI(api_key="sk-None-jB9OBvGOXBWVHo0Z4Yu8T3BlbkFJEHEtK8V4N3cpjTQ2mWH6")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
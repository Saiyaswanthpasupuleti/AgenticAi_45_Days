from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    api_key=os.getenv("api_key"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are a helpful assistant that can answer questions and help with tasks.
if user asks what is 2+2, you should answer 4
example:
input: what is 2+2
output: The answer for the given question is 4
example 2:
input: what is 12+232
output: The answer for the given question is 244
example 3:
input: what is 12-2
output: The answer for the given question is 10
example 4:
input: what is 12/2
output: The answer for the given question is 6
example 5:
input: what is 12*2
output: The answer for the given question is 24
example 6:
"""
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is 12+232-33%12?"}
    ]
)

print(response.choices[0].message.content)
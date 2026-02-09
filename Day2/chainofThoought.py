from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("api_key"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are a helpful AI assistant.

You MUST follow this workflow for every response:
1. START – acknowledge the question
2. PLAN – explain how you will solve it
3. EXECUTE – give the final answer

STRICT RULES:
- Respond ONLY in valid JSON
- Do NOT add extra text
- JSON format must be exactly:

output format:
{
  "step": "START | PLAN | EXECUTE",
  "content": "string"
}

Example:

User: what is 2+2%2-1

you should respond in this format:
{
  "step": "START | PLAN | EXECUTE",
  "content": "string"
}
Example:
User: what is 2+2%2-1

you should respond in this format:
{
  "step": "START | PLAN | EXECUTE",
  "content": "string"
}
Example:
START:
{"step":"START","content":"Received a math expression to solve"}

PLAN:
{"step":"PLAN","content":"Apply BODMAS rule to evaluate the expression"}

EXECUTE:
{"step":"EXECUTE","content":"The final answer is 3"}
"""

messages = [
    {"role": "system", "content": system_prompt}
]

print("AI Agent Started 🚀 (type 'exit' to quit)\n")

while True:
    user_query = input("=> ")

    if user_query.lower() == "exit":
        print("Agent stopped 👋")
        break

    messages.append({"role": "user", "content": user_query})

    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=messages,
        response_format={"type": "json_object"}
    )

    raw_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": raw_response})
    parsed_response = json.loads(raw_response)

    if parsed_response.get("step") == "START":
        print("started ....",parsed_response.get("content"))
        continue
    if parsed_response.get("step") == "PLAN":
        print("planning ....",parsed_response.get("content"))
        continue
    if parsed_response.get("step") == "EXECUTE":
        print("executing ....",parsed_response.get("content"))
        break
    

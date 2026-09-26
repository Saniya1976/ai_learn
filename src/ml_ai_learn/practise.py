import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in env.")

client = Groq(api_key=my_api_key)

messages = [
    {
        "role": "system",
        "content": "You are my Gen Z best friend. You roast me literally in every manner possible and scold me."
    },
    {
        "role": "user",
        "content": "I'm already placed in SAP Labs so I'm gonna rest for 10 months and won't do any internship or any other work and just chill and enjoy my life. What do you think about it?"
    },
    {
        "role": "user",
        "content": "Hello are you aware of Reddit and Quora and all those social media platforms where people share their thoughts and opinions?"
    },
    {
        "role": "user",
        "content": "Which street food is the best in India?"
    },
]

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    temperature=1.0,
    messages=messages,
    max_tokens=900
)

usage = response.usage

print(
    f"Prompt: {messages[-1]['content']} --> "
    f"Prompt tokens: {usage.prompt_tokens}, "
    f"Completion tokens: {usage.completion_tokens}, "
    f"Total tokens: {usage.total_tokens}"
)
print(
    f"Prompt: {messages[-2]['content']} --> "
    f"Prompt tokens: {usage.prompt_tokens}, "
    f"Completion tokens: {usage.completion_tokens}, "
    f"Total tokens: {usage.total_tokens} finish reasons: {response.choices[0].finish_reason}"
)

# print(response.choices[0].message.content)
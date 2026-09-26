import os
import json
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Create Groq client
client = Groq(api_key=my_api_key)


# -----------------------------
# Pydantic Model
# -----------------------------

class Ticket(BaseModel):
    name: str = Field(description="The user's full name")
    email: str = Field(description="The user's email address")
    degree: str = Field(description="The user's current degree program")
    institute: str = Field(description="The user's educational institute")
    brother_name: str = Field(description="The user's brother's name")
    issue: str = Field(description="The user's issue or request for guidance")


# -----------------------------
# Customer Ticket
# -----------------------------

text = """
Hello my name is Saniya and I am currently pursuing BCA degree
from Maharaja Surajmal Institute and my email is saniya234@gmail.com.
My brother's name is Prince and my sister's name is Maniya.
i am not able to get any internship opportunities in my field and I am looking for some guidance on how to get started with internships.
"""


# -----------------------------
# Prompt
# -----------------------------

messages = [
    {
        "role": "system",
        "content": """
You are a helpful information extraction assistant.

Extract the required information from the customer ticket.
Return ONLY valid JSON matching the provided schema.

If a field is not mentioned in the ticket, use an empty string.
Do not add extra fields.
"""
    },
    {
        "role": "user",
        "content": f"""
Customer ticket:

{text}
"""
    }
]


# -----------------------------
# JSON Schema
# -----------------------------

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "ticket",
        "schema": schema
    }
}


# -----------------------------
# Groq API Call
# -----------------------------

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages,
    response_format=response_format,
    max_tokens=500,
    temperature=0.2
)


# -----------------------------
# Get model response
# -----------------------------

result = response.choices[0].message.content

print(result)


# -----------------------------
# Validate with Pydantic
# -----------------------------

ticket = Ticket.model_validate_json(result)

print("\nValidated Pydantic object:")
print(ticket)

print("\nName:", ticket.name)
print("Email:", ticket.email)
print("Degree:", ticket.degree)
print("Institute:", ticket.institute)
print("Issue:", ticket.issue)
print("Brother:", ticket.brother_name)



# from pydantic import BaseModel, EmailStr

# class User(BaseModel):
#     id: int
#     name: str
#     email: EmailStr
#     age: int | None = None  # optional

# data = {
#     "id": "10",          # will be coerced to int
#     "name": "Saniya",
#     "email": "saniya@example.com",
#     "age": "22"          # will be coerced to int
# }

# user = User(**data)
# print(user)
# # User(id=10, name='Saniya', email='saniya@example.com', age=22)
# print(user.model_dump())  # dict representation
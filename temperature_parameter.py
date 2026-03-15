from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("GROQ_API_KEY not set. Add it to a .env file or your environment.")
    raise SystemExit(1)

# API configuration
GROQ_MODEL_NAME = "llama-3.1-8b-instant"

# Initialize client
client = Groq(api_key=GROQ_API_KEY)

# Prompt
prompt = "Discuss about Naruto anime"

# Temperature values to test creativity
temperatures = [0, 0.5, 1]

for temp in temperatures:
    response = client.chat.completions.create(
        model=GROQ_MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temp
    )

    print("\n-----------------------------")
    print("Temperature:", temp)
    print(response.choices[0].message.content)
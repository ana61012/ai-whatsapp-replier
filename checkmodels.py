from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Ensure this grabs your key correctly
api_key = os.getenv("GEMINI_KEY")
client = genai.Client(api_key=api_key)

print("---------------------------------------------")
print("   AVAILABLE MODELS FOR YOUR KEY")
print("---------------------------------------------")

try:
    # In the new SDK, we just iterate and print the name directly
    for m in client.models.list():
        print(f"ID: {m.name}")
        
except Exception as e:
    print(f"Error: {e}")
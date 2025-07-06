from dotenv import load_dotenv
import os
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY environment variable is not set.")
openai.api_key = OPENAI_API_KEY
client = openai
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key=os.getenv('API_Key'))

text = input("Prompt: ") or "The cat sat on the mat"
embeddings = client.models.embed_content(
    model = "gemini-embedding-2",  # gemini-3.8-flash is overloaded right now
    contents = text
)

print(embeddings.embeddings[0].values)
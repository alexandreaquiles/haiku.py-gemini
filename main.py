import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 0,
  "max_output_tokens": 1800,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Você é um poeta brasileiro com herança japonesa que escreve poemas no estilo haiku.\nVocê deve escrever apenas uma estrofe. Use muitos emojis.",
)

response = model.generate_content("Gere um poema sobre a fumaça no Brasil em 2024.")

print(response.text)
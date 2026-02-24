import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar API Key
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Configuración del chat
config = types.GenerateContentConfig(
    max_output_tokens=2018,
    system_instruction="Eres un asistente educativo especializado en Inteligencia Artificial"
    ". Si alguien no habla de inteligencia artificial responde que no sabes, además tienes que responder en menos de 50 palabras"
)

chat = client.chats.create(
    model="gemini-3-flash-preview", 
    config=config)

print("--- Ejercicio 1: Consulta sobre IA ---")
pregunta = input("Ingresa tu pregunta sobre IA :")

try:
    respuesta = chat.send_message(pregunta)
    print(f"\nAsistente: {respuesta.text}")
except Exception as e:
    print(f"Error al procesar la solicitud: {e}")


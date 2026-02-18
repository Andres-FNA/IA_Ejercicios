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
    max_output_tokens=2048,
    system_instruction=(
        "Eres un vendedor amable en una tienda de tecnología. "
        "Responde con claridad, precisión y simpatía."
    )
)

chat = client.chats.create(
    model="gemini-3-flash-preview", 
    config=config)

# Historial precargado (Few-Shot)
historial = [
    {"user": "¿Este portátil tiene pantalla táctil?", 
     "assistant": "Sí, este portátil cuenta con pantalla táctil de 15.6 pulgadas, resolución Full HD y compatible con lápices digitales."},
    {"user": "¿Cuál es la capacidad de la batería del smartphone X?", 
     "assistant": "El smartphone X tiene una batería de 4500 mAh que permite hasta 24 horas de uso continuo y carga rápida de 30W."}
]

# Cargar historial en el chat
for h in historial:
    chat.send_message(h["user"])
    chat.send_message(h["assistant"])

print("--- Ejercicio 3: Chat de Soporte ---")
print("(Escribe 'finalizar' para terminar)\n")

while True:
    user_input = input("Cliente: ")
    if user_input.lower() == "finalizar":
        print("Asistente: ¡Gracias por visitarnos! Hasta pronto.")
        break
    try:
        respuesta = chat.send_message(user_input)
        print(f"Asistente: {respuesta.text}\n")
    except Exception as e:
        print(f"Error al procesar la solicitud: {e}")

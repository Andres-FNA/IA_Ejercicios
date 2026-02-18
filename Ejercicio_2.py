import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Cargar API Key
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=API_KEY)

def procesar_articulo(texto, tarea):
    """
    Procesa un texto según la tarea indicada por el usuario.
    La IA actúa como un Editor Editorial de prestigio.
    """

    config = types.GenerateContentConfig(
        max_output_tokens=3000,
        system_instruction=(
            "Eres un Editor Editorial de prestigio. "
            "Tienes amplia experiencia en redacción académica, técnica y ejecutiva. "
            "Si te piden resumir un texto hazlo de una forma corta y consiza para que nadie se confunda "
            "Si te piden cualquier otra tarea que no sea traducir ni resumir tu estilo debe ser claro, formal, estructurado y profesional. "
            "Cumple rigurosamente la tarea solicitada sobre el texto proporcionado. Si no tiene nada que ver di que no sabes."
        )
    )

    chat = client.chats.create(
        model="gemini-3-flash-preview",
        config=config
    )

    # Prompt dinámico: la tarea la define el usuario
    prompt = f"""
    Tarea solicitada: {tarea}
    Texto:
    {texto}
    """
    respuesta = chat.send_message(prompt)
    return respuesta.text
# Ingreso de datos
print("--- Ejercicio 2: Procesador de Texto Inteligente ---\n")

texto = input("Ingresa el texto a procesar:\n\n")
tarea = input("\n¿Qué deseas hacer con el texto? (Ej: resumir, profesionalizar, traducir, mejorar redacción, analizar tono, etc.):\n\n")

try:
    resultado = procesar_articulo(texto, tarea)
    print("\n--- Resultado ---\n")
    print(resultado)
except Exception as e:
    print(f"Error al procesar la solicitud: {e}")

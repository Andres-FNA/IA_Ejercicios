# IA_Ejercicios Andres Avendaño
# Ejercicios_IA
Proyecto: Integración con Gemini – Ejercicios Prácticos
Descripción

Este proyecto contiene tres ejercicios prácticos desarrollados en Python para interactuar con el modelo Gemini de Google mediante su SDK oficial. El objetivo es aplicar conceptos fundamentales de configuración de modelos, uso de system_instruction, manejo de prompts y construcción de sistemas conversacionales con historial.

Los ejercicios están diseñados para reforzar habilidades en integración de APIs de Inteligencia Artificial y diseño de prompts estructurados.

Requisitos:
Python 3.9 o superior
Cuenta en Google AI Studio
API Key de Gemini
Archivo .env con la variable:
GEMINI_API_KEY=tu_api_key_aqui

Librerías necesarias:
pip install google-genai python-dotenv

Estructura del Proyecto
Ejercicio 1 – Conexión y Petición Básica
Inicializa el cliente de Gemini y realiza una consulta simple relacionada con Inteligencia Artificial. El usuario ingresa la pregunta por teclado y el modelo responde bajo una configuración controlada.

Conceptos aplicados:
Inicialización del cliente
Configuración con GenerateContentConfig
Uso de system_instruction
Interacción básica con el modelo

Evidencia de funcionamiento del ejercicio 1: 
<img width="1227" height="590" alt="image" src="https://github.com/user-attachments/assets/ba16f3ad-46e9-4d07-9fc3-2e6c6fd88fa0" />


Ejercicio 2 – Procesador de Textos Inteligente
Se implementa una función procesar_articulo(texto, tarea) que recibe:
Un texto
Una tarea definida por el usuario (ej. resumir, traducir, analizar, profesionalizar, etc.)
El modelo actúa como un Editor Editorial de prestigio, definido mediante system_instruction, y ejecuta la tarea solicitada sobre el texto proporcionado.

Conceptos aplicados:
Prompt dinámico
Rol especializado del modelo
Procesamiento flexible de texto
Ingeniería de prompts
Evidencia de funcionamiento del ejercicio 2:
<img width="1232" height="1016" alt="image" src="https://github.com/user-attachments/assets/b77bd550-058c-4c20-b5df-84a0b41526c4" />

Ejercicio 3 – Chat de Soporte con Historial (Few-Shot)
Construcción de un sistema conversacional para una tienda de tecnología.

Características:
Rol definido como vendedor amable
Historial precargado (few-shot learning)
Interacción continua hasta que el usuario escriba "finalizar"
Conceptos aplicados:
Conversación multi-turno
Contexto previo (few-shot prompting)
Simulación de caso real de negocio
Evidencia de funcionamiento del ejercicio 3:<img width="1212" height="824" alt="image" src="https://github.com/user-attachments/assets/36de5398-84ae-418b-b4f9-ca380ecd5659" />


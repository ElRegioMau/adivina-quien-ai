import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

CHARACTER = "pelo rubio, gafas, sombrero, mujer"

def ask_gpt(question):
    prompt = f"""Estás jugando Adivina Quién. Tú eres un personaje con estas características: {CHARACTER}.
Responde solo con "Sí", "No" o "No puedo responder a eso" a esta pregunta: {question}"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content'].strip()

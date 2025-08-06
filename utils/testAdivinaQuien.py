import google.generativeai as genai

API_KEY = "AIzaSyAvsFMaXKKndFYz4_TU_thn7kekzvjO8po"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

def formatear_contexto(contexto):
    texto = ""
    for i, (pregunta, respuesta) in enumerate(contexto, 1):
        texto += f"{i}. Pregunta: {pregunta}\n   Respuesta: {respuesta}\n"
    return texto

def armar_prompt(contexto):
    if not contexto:
        return (
            "Estamos jugando a 'Adivina Quién'. Tú (IA) eres quien debe adivinar en qué personaje estoy pensando. "
            "Puede ser real o ficticio (ej: Donald Trump, Bart Simpson, AMLO, Mi mascota, Harry Potter, etc.).\n\n"
            "Solo tú haces preguntas para tratar de adivinar quién es, y yo solo respondo 'sí', 'no', 'no sé' o 'salir'.\n"
            "Muy importante, nos encontramos en el 2025. Aclara al usuario hasta que fecha llega tu conocimiente'.\n"
            "Comienza con una pregunta para reducir opciones (ej: ¿Es hombre?, ¿Es real?, etc.)."
        )
    else:
        contexto_texto = formatear_contexto(contexto)
        return (
            "Estamos jugando a 'Adivina Quién'. Tú (IA) haces preguntas y yo respondo con 'sí', 'no', 'no sé'.\n"
            "Aquí está el historial hasta ahora:\n\n"
            f"{contexto_texto}\n\n"
            "Si tienes suficientes pistas, intenta adivinar el personaje con un nombre concreto. "
            "Si no, haz otra pregunta cerrada para reducir las opciones."
        )


def jugar_adivina_quien():
    print("Piensa en un personaje (real o ficticio). Yo intentaré adivinarlo.")
    contexto = []

    while True:
     prompt = armar_prompt(contexto)
     respuesta_ia = model.generate_content(prompt).text.strip()
     print("\nIA:", respuesta_ia)

    # Si la IA intenta adivinar un personaje con nombre propio
     if any(palabra in respuesta_ia.lower() for palabra in ["es ", "mi adivinanza es", "yo diría que", "creo que tu personaje es"]):
        usuario = input("¿Adiviné? (si/no/adivinaste/salir): ").strip().lower()
        if usuario == "adivinaste":
            print("¡Genial! Gracias por jugar.")
            break
        elif usuario == "salir":
            print("Gracias por jugar.")
            break
        else:
            contexto.append((respuesta_ia, usuario))
            continue

    # Si solo es una pregunta más, se responde
    usuario = input("Responde (si/no/no se/salir): ").strip().lower()
    if usuario == "salir":
        print("Gracias por jugar.")
        
    contexto.append((respuesta_ia, usuario))

if __name__ == "__main__":
    jugar_adivina_quien()

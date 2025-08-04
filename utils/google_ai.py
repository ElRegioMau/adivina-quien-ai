import os
from google.cloud import texttospeech, language_v1

# Configura tu API Key (puedes usar variables de entorno)
os.environ["GOOGLE_API_KEY"] = "AIzaSyAvsFMaXKKndFYz4_TU_thn7kekzvjO8po"

def get_first_question():
    # Puedes personalizar la lógica inicial
    return "¿Tu personaje es hombre?"

def get_next_question(answer, context):
    # Aquí puedes usar Google Natural Language para generar la siguiente pregunta
    # Ejemplo simple:
    if answer == "Si":
        return "¿Tu personaje tiene gafas?"
    elif answer == "No":
        return "¿Tu personaje tiene sombrero?"
    else:
        return "¿Tu personaje tiene barba?"

def synthesize_speech(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-ES", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )
    return response.audio_content
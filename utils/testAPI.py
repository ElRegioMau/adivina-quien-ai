import google.generativeai as genai

# Tu API Key (recuerda revocar después de probar)
API_KEY = "AIzaSyAvsFMaXKKndFYz4_TU_thn7kekzvjO8po"

# Configura la API
genai.configure(api_key=API_KEY)

# Crea una instancia del modelo Gemini
model = genai.GenerativeModel("gemini-2.5-flash")

# Realiza una prueba de conversación
response = model.generate_content("¿Quién fue Albert Einstein?")

# Imprime la respuesta
print("Respuesta de Gemini:")
print(response.text)

import google.generativeai as genai

genai.configure(api_key="AIzaSyAvsFMaXKKndFYz4_TU_thn7kekzvjO8po")

models = genai.list_models()
print("Modelos disponibles:")
for model in models:
    print(f"- {model.name}")

import ollama

MODELO = "llama3.1:8b"

historial = [
    {"role": "system", "content": "Eres un asistente amable que responde en español de forma clara y breve."}
]

print("Chatbot listo. Escribe 'salir' para terminar.\n")

while True:
    pregunta = input("Tú: ")
    if pregunta.strip().lower() == "salir":
        break

    historial.append({"role": "user", "content": pregunta})
    respuesta = ollama.chat(model=MODELO, messages=historial)
    texto = respuesta["message"]["content"]
    historial.append({"role": "assistant", "content": texto})

    print(f"\nBot: {texto}\n")
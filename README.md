# Chatbot local con IA

Chatbot de terminal que conversa usando un modelo de lenguaje que corre localmente con [Ollama](https://ollama.com), sin depender de servicios en la nube.

## Funcionalidades

- Conversación en español con un modelo Llama 3.1 de 8B parámetros
- Memoria de la conversación: el bot recuerda lo dicho previamente en la sesión
- Respuestas en tiempo real (streaming), mostradas conforme el modelo las genera

## Cómo funciona

El programa mantiene un historial de mensajes con roles (`system`, `user` y `assistant`) y lo envía completo al modelo en cada turno. El mensaje `system` define el comportamiento del asistente.

## Requisitos

- Python 3.10 o superior
- [Ollama](https://ollama.com) instalado
- Se recomienda una GPU con al menos 8 GB de VRAM
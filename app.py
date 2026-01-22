import chainlit as cl
from groq import Groq

client = Groq()

SYSTEM_PROMPT = """Eres un simulador de casos veterinarios."""

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [{"role": "system", "content": SYSTEM_PROMPT}])
    await cl.Message(content="Bienvenido al simulador. ¿Deseas seleccionar un caso por especie o por área temática?").send()

@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )

    assistant_message = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_message})

    await cl.Message(content=assistant_message).send()

import chainlit as cl
from groq import Groq

# LLM client
client = Groq()

SYSTEM_PROMPT = """Eres un simulador de casos veterinarios."""

@cl.on_chat_start
async def start():
    # Initialize chat history with system prompt
    cl.user_session.set("history", [{"role": "system", "content": SYSTEM_PROMPT}])
    # Send first message
    await cl.Message(content="Bienvenido al simulador de casos **veterinarios**.\n\n¿Deseas seleccionar un caso por especie o por área temática?").send()

@cl.on_message
async def main(message: cl.Message):
    # Append user message to history
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    # Generate response from LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )

    # Append LLMs response to history
    assistant_message = response.choices[0].message.content or ""
    history.append({"role": "assistant", "content": assistant_message})

    # Send LLMs response
    await cl.Message(content=assistant_message).send()

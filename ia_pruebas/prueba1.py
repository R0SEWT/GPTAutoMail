import os
from openai import OpenAI


OPENAI_API_KEY = input("Autentificate con tu API-KEY: ")

prompt = input("Digita el prompt: ")


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get(OPENAI_API_KEY),
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)

respuesta = chat_completion.choices[0].message.content

print(respuesta)
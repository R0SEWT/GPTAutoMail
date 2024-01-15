from openai import OpenAI


def get_respuesta_GPT(prompt):
  OPENAI_API_KEY = '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'
  client = OpenAI(api_key=OPENAI_API_KEY)
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
  ]
)
  respuesta = chat_completion.choices[0].message.content
  return respuesta




'''OPENAI_API_KEY = input("Autentificate con tu API-KEY: ")
prompt = input("Digita el prompt: ")

client = OpenAI(api_key=OPENAI_API_KEY)

chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

respuesta = chat_completion.choices[0].message.content

print(respuesta)

'''
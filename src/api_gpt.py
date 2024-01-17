from openai import OpenAI


def get_respuesta_GPT(prompt, OPENAI_API_KEY): 
  client = OpenAI(api_key=OPENAI_API_KEY)
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
  ]
)
  respuesta = chat_completion.choices[0].message.content
  costo = chat_completion['usage']['total_tokens']
  return respuesta, costo

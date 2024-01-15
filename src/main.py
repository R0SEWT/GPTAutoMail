import pandas as pd
import enviar_mails
import c_empleado
import api_gpt
from decouple import config

# cargar BD y prompt personalizado
path = './src/empleados.xlsx'

empleados = []
for index, row in pd.read_excel(path).iterrows():
    empleado = c_empleado.Empleado(row['Nombre'], row['Apellidos'], row['Correo'], row['Cargo'], row['Edad'])
    empleados.append(empleado)

# para cada uno obtener respuesta del chatgpt y mandar por correo
API_OPEN_AI_KEY = config('API_OPEN_AI_KEY')
APP_PASS_GMAIL = config('APP_PASS_GMAIL')

for e in empleados:
    asunto = f"{e.name} nos preocupamos por tu seguridad"
    cuerpo = api_gpt.get_respuesta_GPT(e.prompt, API_OPEN_AI_KEY)
    print(f"Cuerpo del mensaje recibido")
    # inicializar el mensaje y enviarlo 
    enviar_mails.get_and_send_email(e.mail, asunto, cuerpo, APP_PASS_GMAIL)
    print(f"Correo enviado a {e.name} en {e.mail}")
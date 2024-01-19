import pandas as pd
import enviar_mails
import c_empleado
import api_gpt
from decouple import config


def get_empleados_with_prompts(path):
    empleados = []
    for _ ,row in pd.read_excel(path).iterrows():
        empleado = c_empleado.Empleado( row['Nombre'], row['Apellidos']
                                       , row['Correo'], row['Cargo'], row['Edad'],
                                        row['Cantidad de accidentes'], 
                                        row['Años de experiencia'])
        empleados.append(empleado)
    return empleados


def read_env():
    API_OPEN_AI_KEY = config('API_OPEN_AI_KEY')
    EMAIL_ACCOUNT = config('EMAIL_ACCOUNT')
    APP_PASS_GMAIL = config('APP_PASS_GMAIL')
    return API_OPEN_AI_KEY, EMAIL_ACCOUNT, APP_PASS_GMAIL


def gpt_request_and_send(empleados, API_OPEN_AI_KEY, EMAIL_ACCOUNT, APP_PASS_GMAIL):
    total = 0
    for e in empleados:
        asunto = f"{e.name} nos preocupamos por tu seguridad"
        cuerpo, costo = api_gpt.get_respuesta_GPT(e.prompt, API_OPEN_AI_KEY)
        print(f"Cuerpo del mensaje recibido")
        # inicializar el mensaje y enviarlo 
        enviar_mails.get_and_send_email(e.mail, asunto, cuerpo, EMAIL_ACCOUNT, APP_PASS_GMAIL)
        print(f"Correo enviado a {e.name} en {e.mail}. {costo} tokens gastados.")
        total += costo
    return costo     
#####################################################################################################
        
def main():
    # cargar BD y prompts
    path = './src/empleados.xlsx'
    empleados = get_empleados_with_prompts(path)
    precio_token = 0.0000004 #dolares para gpt3.5

    # para cada uno obtener respuesta del chatgpt y mandar por correo
    API_OPEN_AI_KEY, EMAIL_ACCOUNT, APP_PASS_GMAIL = read_env()
    c_tokens = gpt_request_and_send(empleados, API_OPEN_AI_KEY, EMAIL_ACCOUNT, APP_PASS_GMAIL)# Logs
    print(f'Se han gastado {precio_token*c_tokens} dolares')


if __name__ == "__main__":
    main()
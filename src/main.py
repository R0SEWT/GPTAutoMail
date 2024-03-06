import pandas as pd
import enviar_mails
import c_empleado
import api_gpt
from decouple import config


def get_empleados_with_prompts(path):
    """
    Lee información de empleados desde un (.xlsx) 

    Devuelve list con instancias de la clase Empleado o vacio
    """
    try:
        empleados = []
        df = pd.read_excel(path)

        for _, row in df.iterrows():
            empleado = c_empleado.Empleado(
                row['Nombre'], row['Apellidos'],
                row['Correo'], row['Cargo'], row['Edad'],
                row['Cantidad de accidentes'],
                row['Años de experiencia']
            )
            empleados.append(empleado)
            # break ##############################################DEV MODE ####################################

        return empleados

    except Exception as e:
        print(f"Error 0: Error al leer el archivo ({path}): {e}")
        return []


def read_env():
    """
    Lee configuraciones desde un (.env)
    
    Devuelve un dict con las configs o vacio
    """

    try:
        API_OPEN_AI_KEY = config('API_OPEN_AI_KEY')
        EMAIL_ACCOUNT = config('EMAIL_ACCOUNT')
        APP_PASS_GMAIL = config('APP_PASS_GMAIL')
        return {
            'API_OPEN_AI_KEY' : API_OPEN_AI_KEY,
            'EMAIL_ACCOUNT' : EMAIL_ACCOUNT, 
            'APP_PASS_GMAIL': APP_PASS_GMAIL
        }
    
    except Exception as e:
        print(f"Error 1: Error al leer las configuraciones (.env): {e}")
        return {}


def gpt_request_and_send(empleados, config): ######################SEPARAR LA LOGICA #######################
    API_KEY = config['API_OPEN_AI_KEY']
    REMTT = config['EMAIL_ACCOUNT']
    REMTT_PASS = config['APP_PASS_GMAIL']
    total_tokens = 0
    
    for e in empleados:
        asunto = f"{e.name} nos preocupamos por tu seguridad"
        try:
            cuerpo, costo = api_gpt.get_respuesta_GPT(e.prompt, API_KEY)
            print(f"Cuerpo del mensaje recibido \n{cuerpo}\n {costo} tokens gastados.")

            total_tokens += costo

            # inicializar el mensaje y enviarlo 
            enviar_mails.get_and_send_email(e.mail, asunto, cuerpo, REMTT, REMTT_PASS)
            print(f"Correo enviado a {e.name} en {e.mail}.")
            
            print(f'Estado: Gastando {total_tokens} tokens')
            
        except Exception as exc:
            print(f"Error 2: Error al procesar al empleado {e.name}: {exc}")

    return total_tokens     

        
def main():
    # cargar BD y prompts
    path = './src/empleados.xlsx'
    empleados = get_empleados_with_prompts(path)

    PRECIO_TOKEN = 0.0030 / 1000  #dolares para gpt3.5: 0.0030 / 1K tokens

    # para cada uno obtener respuesta del chatgpt y mandar por correo
    config = read_env()
    if config and empleados:
        try:
            c_tokens = gpt_request_and_send(empleados, config)
            c_total = c_tokens * PRECIO_TOKEN
            print(f'Se han gastado {c_tokens} tokens y {c_total} dolares')
        except Exception as e:
            print(f"Error en el proceso principal: {e}")
    else:
        print('Ocurrio un Error de configuracion.\nNo es posible enviar correos.')


if __name__ == "__main__":
    main()
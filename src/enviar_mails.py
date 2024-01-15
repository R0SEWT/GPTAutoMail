from email.message import EmailMessage          # forma del mensaje
import smtplib                                  # se encarga de la conexion con gmail 


def get_email(remitente, destinatario, asunto, cuerpo):
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = asunto
    email.set_content(cuerpo)
    return email


def send_email(smtp_usuario, smtp_contrasena, email):
    # configuracion de conexion 
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Iniciar conexión segura
    server.login(smtp_usuario, smtp_contrasena)
    # enviar el correo
    server.send_message(email)
    # cerrar la conexión
    server.quit()


def get_and_send_email(destinatario, asunto, cuerpo, smtp_contrasena):
    remitente = "rody.vilchez00@gmail.com"
    email = get_email(remitente, destinatario, asunto, cuerpo)
    # establecer conexión con el servidor SMTP y enviar el mensaje
    smtp_usuario = remitente
    send_email(smtp_usuario, smtp_contrasena, email)

'''# config 
remitente = "rody.vilhcez00@gmail.com"
destinatario = "dabat74405@regapts.com"
asunto = "HI"
cuerpo = "Hola mundo"

# inicializar el mensaje
email = get_email(remitente, destinatario, asunto, cuerpo)

# establecer conexión con el servidor SMTP y enviar el mensaje
smtp_usuario = "rody.vilchez00@gmail.com"
smtp_contrasena = 'uhdp wwkk rhne vuep'
'''
#send_email(smtp_usuario, smtp_contrasena, email)

#get_and_send_email('dabat74405@regapts.com', 'hi', 'hola')
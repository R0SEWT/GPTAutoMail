# Proyecto: Envio de correos con respuestas generadas por GPT

Este proyecto utiliza el lenguaje de programación Python y varias bibliotecas para cargar datos personales desde un archivo Excel, generar respuestas mediante OpenAI's GPT, y enviar correos electrónicos personalizados a un grupo de empleados de una empresa electrica fomentando el uso de EPP.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instaladas las siguientes bibliotecas de Python. Puedes instalarlas usando el comando `pip install <nombre_biblioteca>`.

- pandas
- openai
- smtplib
- EmailMessage
- python-decouple 

Además, necesitarás una clave API de OpenAI, así como información de configuración para el envío de correos electrónicos. Estos datos se deben almacenar en un archivo `.env`. No te olvides de añadir el .gitignore ;)

## Estructura de archivos

- `main.py`: El archivo principal que ejecuta el programa.
- `empleados.xlsx`: Archivo Excel que contiene la información de los empleados, incluyendo nombre, apellidos, correo, cargo y edad.
- `enviar_mails.py`: Módulo para enviar correos electrónicos.
- `c_empleado.py`: Módulo que define la clase Empleado.
- `api_gpt.py`: Módulo para realizar solicitudes a la API de GPT.

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto con la siguiente estructura y completa los valores correspondientes:

    ```env
    API_OPEN_AI_KEY=your_openai_api_key
    EMAIL_ACCOUNT=your_email_account
    APP_PASS_GMAIL=your_app_password
    ```

## Ejecución

1. Ejecuta el programa usando el siguiente comando:

    ```bash
    python main.py
    ```

El programa leerá la información de los empleados desde `empleados.xlsx`, generará respuestas utilizando la API de GPT y enviará correos electrónicos personalizados a cada empleado.

**Nota:** Asegúrate de tener una conexión a Internet para realizar solicitudes a la API de GPT. Además, ten cuidado con la frecuencia de uso de la API para evitar exceder los límites de tu cuenta, aqui no vigilamos los tokens ni le tenemos miedo a la muerte.
# Automatización de Correos para Fomentar el Uso de Equipos de Protección Personal (EPP) con Chat-GPT

Este proyecto utiliza Python y diversas bibliotecas para automatizar el proceso de envío de correos electrónicos personalizados a empleados, con el fin de fomentar el uso de Equipos de Protección Personal (EPP) en una empresa de suministro electrico. Se basa en la personalización de mensajes de correo electrónico en función de la `edad`, el `cargo` y los `años de experiencia` de cada empleado.

El proyecto se centra en la eficiencia y la personalización, lo que permite crear mensajes de correo electrónico que sean relevantes y útiles para cada individuo. Este enfoque se alinea con las mejores prácticas recomendadas por Thorium Labs para la implementación de campañas de correo electrónico impulsadas por IA.

Se han utilizado varias bibliotecas de Python para facilitar la automatización del proceso. Entre ellas se incluyen pandas para la manipulación de datos, openai para la interacción con la API de GPT, smtplib para el envío de correos electrónicos y python-decouple para manejar variables de configuración.

La información de los empleados se carga desde un archivo Excel, lo que permite una gestión sencilla y eficiente de los datos. Una vez cargados los datos, se utilizan para generar correos electrónicos personalizados utilizando la API de OpenAI GPT.

Este proyecto no sólo demuestra la capacidad de automatizar tareas repetitivas, sino también la aplicabilidad de la inteligencia artificial en el ámbito de la comunicación corporativa.

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

**Nota:** Asegúrate de tener una conexión a Internet para realizar solicitudes a la API de GPT. Además, ten cuidado con la frecuencia de uso de la API para evitar exceder los límites de tu cuenta.
 **De momento  no vigilamos los tokens ni le tenemos miedo a la muerte.**
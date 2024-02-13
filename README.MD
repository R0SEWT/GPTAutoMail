# Automatización de Correos para Fomentar el Uso de Equipos de Protección Personal (EPP) con Chat-GPT API

## Introducción

Este proyecto te ayuda a enviar correos electrónicos personalizados a tus empleados para recordarles usar sus Equipos de Protección Personal (EPP). Aquí te explicamos cómo funciona y cómo usarlo.

## ¿Qué hace este proyecto?

- Envía correos electrónicos personalizados a empleados.
- Personaliza los mensajes según la `edad`, `cargo` y `años de experiencia` del empleado.
- Ayuda a fomentar el uso de EPP en empresas de suministro eléctrico.

## ¿Cómo preparar mi entorno?

1. Instala las bibliotecas de Python: `pip install pandas openai smtplib EmailMessage python-decouple`
2. Crea un archivo `.env` con tu clave API de OpenAI y detalles de envío de correo electrónico.
3. Ejecuta el programa con el comando: `python main.py`

## ¿Cómo uso el programa?

1. Carga la información de los empleados desde un archivo Excel.
2. El programa genera correos electrónicos personalizados y los envía.

## Fundamento
El proyecto se centra en la eficiencia y la personalización, lo que permite crear mensajes de correo electrónico que sean relevantes y útiles para cada individuo. Este enfoque se alinea con las mejores prácticas recomendadas por Thorium Labs para la implementación de campañas de correo electrónico impulsadas por IA.


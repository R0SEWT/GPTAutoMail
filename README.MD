# Automatización de Correos para Fomentar el Uso de Equipos de Protección Personal (EPP) con Chat-GPT API

## Introducción

Este proyecto usa IA para generar correos personalizados para tus empleados y los envia con el objetivo de promover el uso de sus Equipos de Protección Personal (EPP). 

## Fundamento
El proyecto se centra en la eficiencia y la personalización, lo que permite crear mensajes de correo electrónico que sean relevantes y útiles para cada individuo. Este enfoque se alinea con las mejores prácticas recomendadas por Thorium Labs para la implementación de campañas de correo electrónico impulsadas por IA.

## Diagrama de funcionamiento
### Flujograma de funcionamiento
<img src= assets/flujograma-funcionamiento.png alt= 'Carmencita Lara'>

### Flujograma de metodo de generacion y envio
<img src= assets/flujograma-correo.png alt= 'Carmencita Lara'>

## ¿Cómo preparar mi entorno?

1. Activa el entorno virtual usando `.\env\Scripts\activate` el proyecto usa Python 3.12
1. Instala las bibliotecas de Python: `pip install` pandas openai openpyxl EmailMessage python-decouple
1. Crea un archivo `.env`  con tus credenciales:
```
API_OPEN_AI_KEY = 'API_KEY'
EMAIL_ACCOUNT = 'CORREO_GMAIL'
APP_PASS_GMAIL = 'CLAVE_DE_APLICACION'
```
4. Ejecuta el programa: `python main.py`





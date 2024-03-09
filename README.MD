# Automatización de Correos para Fomentar el Uso de Equipos de Protección Personal (EPP) con Chat-GPT API

<img src= DocAssets/ejemplo.png alt= 'Carmencita Lara ha conspirado contra nosotros'>

## Introducción

Este proyecto usa IA para generar correos personalizados para tus empleados y los envia con el objetivo de promover el uso de sus Equipos de Protección Personal (EPP).

## Fundamento
El proyecto se centra en la eficiencia y la personalización, lo que permite crear mensajes de correo electrónico que sean relevantes y útiles para cada individuo. Este enfoque se alinea con las mejores prácticas recomendadas por Thorium Labs para la implementación de campañas de correo electrónico impulsadas por IA.

## Diagrama de funcionamiento
### Flujograma de funcionamiento
<img src= DocAssets/flujograma-funcionamiento.png alt= 'Carmencita odia los flujogramas'>

### Flujograma de metodo de generacion y envio
<img src= DocAssets/flujograma-correo.png alt= 'Esa mujeeer nunca te amo'>

## ¿Cómo preparar mi entorno?
El proyecto usa Python 3.12

1. Crea un entorno virtual `python -m env venv`
1. Activa el entorno virtual `.\env\Scripts\activate` 
1. Instala las bibliotecas usadas en el proyecto `pip install -r ".\requirements.txt"`
1. Crea un `.env` con tus credenciales:
```
API_OPEN_AI_KEY = 'TU_API_KEY'
EMAIL_ACCOUNT = 'TU_CORREO_GMAIL'
APP_PASS_GMAIL = 'TU_CLAVE_DE_APLICACION'
```
4. Ejecuta el programa: `python src/main.py`





class Empleado:
    def __init__(self, name, lname, mail, rol, age):
       self.name = name
       self.lname = lname
       self.mail = mail
       self.rol = rol
       self.age = age
       self.prompt = f'Asume que eres un ingeniero de seguridad industrial y debes enviar un mensaje para convencer a un trabajador de {age} años para que use su equipo de protección personal. El trabajdor se dedica a {rol} No menciones la edad en el  mensaje. El mensaje debe ser de un párrafo y el lenguaje debe ser amigable. El mensaje debe estar dirigido a "{name} {lname}. A continuación debes sugerir el equipo de seguridad industrial adecuado para la actividad. Firma como Juan Perez'

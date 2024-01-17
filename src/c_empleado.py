class Empleado:
    def __init__(self, name, lname, mail, rol, age, n_accdt, n_xp):
       self.name = name
       self.lname = lname
       self.mail = mail
       self.rol = rol
       self.age = age
       self.n_accdt = n_accdt
       self.n_xp = n_xp
       self.prompt = f"""Asume que eres un ingeniero de seguridad industrial y debes 
                enviar un mensaje para convencer a un trabajador de {age} años para que use 
                su equipo de protección personal. El colaborador realiza sus labores en una 
                empresa de distribución eléctrica y se dedica a {rol}, tiene {n_xp} años de
                experiencia y ha sufrido {n_accdt} accidentes en la empresa. No menciones 
                información personal, o sobre la cantidad de accidentes, que no sea la edad o 
                el cargo en el mensaje. El mensaje debe ser de un párrafo y el lenguaje debe
                ser amigable. El mensaje debe estar dirigido a {name} {lname}. A continuación
                debes sugerir el equipo de seguridad industrial adecuado para la actividad. 
                Firma como Juan Perez"""

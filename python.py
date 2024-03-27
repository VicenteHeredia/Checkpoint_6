# Cree una clase de Python llamada Usuario que use el método init
# y cree un nombre de usuario y una contraseña.
# Crea un objeto usando la clase.

class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
    
    def name(self):
        return f"Para el usuario {self.usuario} la contraseña es: {self.contraseña}"
    
usuario_uno = Usuario('Pepe', 'pepe0123')

print(usuario_uno.name())
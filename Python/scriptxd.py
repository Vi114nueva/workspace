class Persona():
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return f'(Persona): {self.nombre} {self.apellido} {self.edad} {self.genero}'
    
p1 = Persona('Jorge', 'Villanueva', 17, 'Hombre')



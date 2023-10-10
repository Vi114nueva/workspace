# Clases
class Galleta():
    def __init__(self, nombre, sabor, color):
        self.nombre = nombre
        self.sabor = sabor
        self.color = color
    
    def imprimir(self):
        print(f'Nombre: {self.nombre} \nSabor: {self.sabor} \nColor: {self.color}')
    
    def __str__(self):
        return f'Galleta: ({self.nombre}, {self.sabor}, {self.color})'
    
class Gaseosa(Galleta):
    def __str__(self):
        return f'Gaseosa: ({self.nombre}, {self.sabor}, {self.color})'
        
galleta1 = Galleta('Oreo', 'Dulce', 'Negro')
print(galleta1)

gaseosa1 = Gaseosa('Coca Cola', 'Dulce', 'Negro')
print(gaseosa1)
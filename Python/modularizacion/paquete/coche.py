class Coche():
    def __init__(self, ruedas, puertas, color):
        self.ruedas = ruedas
        self.puertas = puertas
        self.color = color
        self.enmarcha = False
    
    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return 'El coche esta enmarcha'
        else:
            return 'El coche no esta enmarcha'

    def estado(self):
        return f'Ruedas: {self.ruedas} \nPuertas: {self.puertas} \nColor: {self.color} \nEnmarcha: {self.enmarcha}'

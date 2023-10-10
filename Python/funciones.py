# Funciones
def saludar(nombre):
    print(f'Hola, {nombre} desde la funcion.')

def sumar(a, b):
    return a + b

nombre = input('Ingrese su nombre: ')

saludar(nombre)

a = int(input('Ingrese N01: '))
b = int(input('Ingrese N02: '))

suma = sumar(a, b)
print(f'La suma de {a} + {b} = {suma}')
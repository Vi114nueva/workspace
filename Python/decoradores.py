def decorador(func):
    def decorar(*args):
        print('Inicio la ejecucion de la funcion ' + func.__name__)
        func(*args)
        print('Termino la ejecucion de la funcion ' + func.__name__)
    
    return decorar

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')
    
@decorador
def sumar(a, b):
    suma = a + b
    print(suma)
    
saludar('Jorge')
sumar(5, 10)
def sumar(*args):
    suma = 0
    for n in args:
        suma += n
    
    return suma
    
suma = sumar(1,2,3,4,5)
print(suma)

def datos(nombre, **kwargs):
    print(nombre, kwargs)
    
datos('Jorge', apellido='Villanueva', estado=True)
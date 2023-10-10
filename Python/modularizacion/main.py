from mate import sumar, restar
from paquete.coche import Coche as ch

def main():
    suma = sumar(5, 5)
    print(suma)

    resta = restar(10, 5)
    print(resta)
    
    miCoche = ch(4, 4, 'Negro')
    
    print(miCoche.arrancar(False))
    print(miCoche.estado())
    
if __name__ == '__main__':
    main()
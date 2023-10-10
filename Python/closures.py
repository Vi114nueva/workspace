def can_repetir(n):
    def repetir(t):
        return t * n
    
    return repetir

repetir5veces = can_repetir(2)
print(repetir5veces('Hola'))
# Lista
colores = ['Rojo','Negro', 'Verde']

print(colores)
print(colores[1])

colores[1] = 'Blanco'
print(colores)

colores.append('Azul')
colores.append('Amarillo')
print(colores)

colores.pop()
print(colores)

colores.remove('Verde')
print(colores)

colores.reverse()
print(colores)

tupla = tuple(colores)
print(tupla)

print(tupla[1])
print(len(tupla))
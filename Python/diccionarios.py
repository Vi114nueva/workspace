# Diccionarios
datos = {
    'uno': 1,
    'colores': ['Rojo', 'Negro', 'Verde'],
    'dos': 2
}

print(datos)
print(datos['colores'])

datos['uno'] = 'Uno'
print(datos)

datos['estado'] = True
print(datos)

del datos['dos']
print(datos)
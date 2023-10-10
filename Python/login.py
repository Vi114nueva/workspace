import os

def login(username, password):
    user = False
    data = None
    
    for usuario in database:
        if usuario['username'] == username and usuario['password'] == password:
            user = True
            data = usuario
    
    if user:
        print('Bienvenido.')
    else:
        print('Porfavor ingrese correctamente sus crendenciales.')
    
    return user, data

def menu(data):
    if data['verificado']:
        print('Felicidades eres verificado!!')
    else:
        print('No eres verificado.')
        
    print('1. Mis datos')
    print('2. Salir')
    opc = int(input('> '))
    
    if opc == 1:
        print('Username: ' + data['username'])
        print('Password: ' + data['password'])
        print('Verificado: ' + str(data['verificado']))


database = [
    {
        'username': 'Jorge',
        'password': 'pichona',
        'verificado': True 
    },
    {
        'username': 'pelusa',
        'password': 'pelusa123',
        'verificado': False
    }
]

user = False
while not user:
    username = input('Username: ')
    password = input('Password: ')
    user, data = login(username, password)

menu(data)
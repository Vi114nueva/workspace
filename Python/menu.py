class Message():
    def __init__(self, nombre_envio , nombre_cliente, mensaje_texto):
        self.nombre_envio = nombre_envio
        self.nombre_cliente = nombre_cliente
        self.mensaje_texto = mensaje_texto
        
    def __str__(self):
        return 'Mensaje enviado por: {}, para: {}'.format(self.nombre_envio, self.nombre_cliente)
    
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password   
        self.mensajes = []

def signup():
    print('[Signup]')
    username = input('Nombre de usuario: ')
    password = input('Contraseña: ')
    if username and password:
        new_user = User(username, password)
        db['users'].append(new_user)
        print('Registrado.')
    else:
        print('Completa los campos correctamente.')        

def login():
    print('[Login]')
    username = input('Username: ')
    password = input('Password: ')
    if username and password:
        for user in db['users']:
            if username == user.username and password == user.password:
                print('Bienvenido.')
                return user
    
        print('User not found.')
        return None 
    else:
        print('Completa los campos correctamente.')
        return None
    
def menu_mensajeria(user):
    while user:
        print('[MENU-MENSAJERIA]')
        print('1. Enviar mensaje')
        print('2. Mis mensajes')
        print('3. Salir')
        try:
            opc = int(input('> '))
            
            if opc == 1:
                print('[ENVIAR MENSAJE]')
                msg = input('Message: ')
                nombre_enviar = input('To: ')
                if msg and nombre_enviar:
                    enviado = False
                    new_message = Message(nombre_envio=user.username, nombre_cliente=nombre_enviar, mensaje_texto=msg)
                    
                    for user in db['users']:
                        if user.username == nombre_enviar:
                            user.mensajes.append(new_message)
                            enviado = True

                    if enviado:
                        print('Mensaje enviado.')
                    else:
                        print('No se encontro ningun nombre de usuario.')                        
                    
                else:
                    print('Completa los campos correctamente.')
            
            elif opc == 2:            
                if user.mensajes:
                    print('[MENSAJES]')
                    for msg in user.mensajes:
                        print('[{}] => {}'.format(msg.nombre_envio, msg.mensaje_texto))
                else:
                    print('Messages not found.')
            
            elif opc == 3:
                user = None
            
            else:
                print('Opcion no validad.')
        
        except ValueError:
            print('Ingrese un dijito.')
            
            
    

db = {
    'users': []
}
user = None
salir = False
while not salir:
    print('[MENU]')
    print('1. Iniciar sesion')
    print('2. Registrar')
    print('3. Salir')
    try:
        opc = int(input('> '))
        
        if opc == 1:
            user = login()
            menu_mensajeria(user)
        elif opc == 2:
            signup()
        elif opc == 3:
            salir = True
        else:
            print('Opcion no validad.')
    except ValueError:
        print('Ingrese un dijito.')
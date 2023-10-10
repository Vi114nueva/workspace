import shutil
import os
import time

# src = 'C:/Users/Jorge Villanueva/Desktop/documentos/'
# dest = 'C:/Users/Jorge Villanueva/Desktop/workspace/'

# files = os.listdir(src)

# for f in files:
#     shutil.copy(src + f, dest)
    

dir = os.environ['USERPROFILE'] + '/Pictures/'
dest = 'C:/Users/Jorge Villanueva/Desktop/workspace/'

print('[*] Comenzando ataque...')
time.sleep(1)

print('[*] Localizando directorio...')
time.sleep(1)

print('[*] Copiando archivos...')
time.sleep(2)

try:
    files = os.listdir(dir)
    for f in files:
        shutil.copy(dir + f, dest)
except:
    print('Algo salido mal!!')
    exit()
    
print('[*] Listo.')
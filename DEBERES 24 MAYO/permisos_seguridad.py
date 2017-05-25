# !/usr/bin/python
# coding:utf-8
#Muestra lo que pesa cada archivo y directorio.

import os
import stat

#Asignar variables 
path_to_explore="/home/guest/Documentos/prueba"
total_size=0

# Mostramos ruta de todo.  
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
#Muestra los archivos que són diferentes a 0, que son inseguros.
        if(permissions <>0):
			print oct(permissions)
        

    for name in dirs:
        name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size
        permissions = stat.S_IMODE ( os.stat (name_path).st_mode )
#Muestra los directorios que són diferentes a 0, que son inseguros.
        if(permissions <>0):
			print oct(permissions)
 
print "El tamaño total en B es:" , total_size

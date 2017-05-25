#! /usr/bin/python
# coding:utf-8

import os
import stat

#Asignamos variables
path_to_explore="/home/guest/Documentos/prueba"

total_size=0

# Mostrem ruta de tot
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
		name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size
        permissions=start.S_IMODE ( os.stat (name_path).st_mode)
        #Muestra los archivos que són diferentes a 0, que son inseguros.
		if(permissions<>0):
			print oct(permissions)

	for name in dirs:
		name_path=os.path.join(root, name)
        print(name_path) ,
        print os.stat(name_path).st_size
        total_size=total_size+os.stat(name_path).st_size
        permissions=start.S_IMODE ( os.stat (name_path).st_mode )
        #Muestra los directorios que són diferentes a 0, que son inseguros.
        print oct (permissions),
        if(permissions<>0):
				print oct(permissions)
        
	print "Tamaño total en Byts:" , total_size

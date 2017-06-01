# coding:utf-8
#!/usr/bin/python

import os
import time
import stat

path_to_explore="./"
totalsize=0

tamanyo_minimo=1073741824
time.ctime(os.path.getatime(path_to_explore))

for root, dirs, files in os.walk(path_to_explore):
	for name in files:
		name_path=os.path.join(root, name)
#Mostramos lo que ocupa cada archivo.
        tamanyo=os.stat(name_path).st_size

if (tamanyo>=2**30) and (time.ctime(os.path.getctime(path_to_explore))):

	print name_path ,
	print time.ctime(os.path.getatime(path_to_explore))

print "Archivos que ocupan más de 1GB:\n", name_path

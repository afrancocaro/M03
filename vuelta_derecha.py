# !/usr/bin/python
# -*-coding: utf-8-*-
#Hcer vuelta completa en dirección a la derecha.
num=1
sortir=False
while(sortir==False):
		print(num)
#Dirección a hacia arriba.
	if(num%8==1 or num%8==2):
		print ("ARRIBA")
#Dirección a hacia la derecha.
	if(num%8==3 or num%8==4):
		print ("DERECHA")
#Dirección a hacia abajo.
	if(num%8==5 or num%8==6):
		print ("ABAJO")
#Dirección a hacia la izquierda y acaba el bucle.
	if(num%8==7 or num%8==0):
		print ("IZQUIERDA")
num=num+1

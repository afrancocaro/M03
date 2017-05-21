# !/usr/bin/python
# -*-coding: utf-8-*-

#Hacer vuelta completa en dirección a la derecha con turnos.
vueltas=1
turnos=0
sortir=False
while(sortir==False):
		print (vueltas, turnos)
#Dirección a hacia la izquierda y hace el segunda vuelta con turno.
	if(vueltas%8==0):
		print ("IZQUIERDA")
		turnos=turnos+1
#Cuando hace el segundo turno sale del bucle.
	if(turnos==2):
		sortir=True
	vueltas=vueltas+1

# !/usr/bin/python
# -*-coding: utf-8-*-

#Hacer vuelta completa en dirección a la derecha con turnos.
vueltas=1
turnos=0
sortir=False
while(sortir==False):
	if(vueltas%8==1 or vueltas%8==2):
		print ("ARRIBA")
#Dirección a hacia la derecha.
	if(vueltas%8==3 or vueltas%8==4):
		print ("DERECHA")
#Dirección a hacia abajo.
	if(vueltas%8==5 or vueltas%8==6):
		print ("ABAJO")
#Dirección a hacia la izquierda.
	if(vueltas%8==7):
		print ("IZQUIERDA")
#Dirección a hacia la izquierda y hace el segunda vuelta con turno.
	if(vueltas%8==0):
		print ("IZQUIERDA")
		turnos=turnos+1
#Cuando hace el segundo turno sale del bucle.
	if(turnos==2):
		sortir=True
	vueltas=vueltas+1

# !/usr/bin/python
# -*-coding: utf-8-*-

j1=read()
j2=read()
if (j1=="piedra")and(j2=="piedra"):
	print ("¡Empate!")
	
if (j1=="piedra")and(j2=="papel"):
	print ("¡Gana el jugador 2!")
	
if (j1=="piedra")and("tijera"):
	print ("¡Gana el jugador 1!")
	
if (j1=="papel")and(j2=="papel"):
	print ("¡Empate!")
	
if(j1=="papel")and("piedra"):
	print ("Gana el jugador 1!")
	
if(j1=="papel")and(j2=="tijera"):
	print ("¡Gana el jugador 2!")
	
if(j1=="tijera")and(j2=="tijera"):
	print ("¡Empate!")
	
if(j1=="tijera")and(j2=="piedra"):
	print ("¡Gana el jugador 2!")
	
if(j1=="tijera")and(j2=="papel"):
	print ("!Gana el jugador 1¡")

# !/bin/bash
#coding:utf-8

#Las cartas tienen un Nª: A,2-10,J,Q,K (total 13).
#Las cartas tienen un palo: picas, treboles, corazones, diamantes (total de 4).

import os
os.system('clear')
import random
from random import randint
salir=False

numeros=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
palos=["Diamantes","Corazones","Treboles","Picas"]

while(salir==False):
#Generamos un numero aleatoriamente de la lista numeros y palos
	j1num=random.choice(numeros)
	j2num=random.choice(numeros)

	j1pal=random.choice(palos)
	j2pal=random.choice(palos)
#Empate
	if (j1num==j2num):
		print "Jugador 1 tiene un ", j1num , "de", j1pal
		print "Jugador 2 tiene un ", j2num , "de", j2pal
		print "Empate!"
	else:
#Ganador
		if (j1num>j2num):
			print "Jugador 1 tiene un ", j1num , "de", j1pal
			print "Jugador 2 tiene un ", j2num , "de", j2pal
			print "Gana Jugado 1!"
		else:
			print "Jugador 1 tiene un ", j1num , "de", j1pal
			print "Jugador 2 tiene un ", j2num , "de", j2pal
			print "Gana Jugador 2!"
	salir=True

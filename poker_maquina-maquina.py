# !/usr/bin/python
# -*-coding: utf-8-*-
#Las cartas tienen un Nª: A,2-10-J-Q,K (total 13).
#Las cartas tienen un palo: corazones, picas, treboles, diamantes (total de 4).
from random import randint
#Generamos la tirada de jugador 1 (coje una carta aleatoria).
j1num=randint(1,13)
j1pal=randint(1,4)
#Generamos la tirada de jugador 2 (coje una carta aleatoria).
j2num=randint(1,13)
j2pal=randint(1,4)
#Comprovamos si hay empate.
if(j1num==j2num):
	print ("Empate")
else:
	if(j1num>j2num):
		print ("Gana jugador 1")
	else:
		print ("Gana jugador 2")

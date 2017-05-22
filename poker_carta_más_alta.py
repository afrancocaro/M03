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

while(sortir==False):
#Jugador 1 coje cartas aleatorias.
	numero1=j1num
	if (j1num==11):
		numero1="J"
	if (j1num==12):
		numero1="Q"
	if (j1num==13):
		numero1="K"

	if (j2pal==1):
		numero1=("Corazones")
	if (j2pal==2):
		numero1=("Treboles")
	if (j2pal==3):
		numero1=("Diamantes")
	if (j2pal==4):
		numero1=("Picas")
#Jugador 2 coje cartas aleatorias.
	numero=j2num
	if (j2num==11):
		numero2=("J")
	if (j2num==12)
		numero2=("Q")
	if (j2num==13):
		numero2=("K")

	if (j2pal==1):
		pal=("Corazones")
	if (j2pal==2):
		pal=("Treboles")
	if (j2pal==3):
		pal=("Diamantes")
	if (j2pal==4):
		pal=("Picas")

	print ("Jugador 1 tiene:",numero1,"de",pal)	
	print ("Jugador 2 tiene:",numero2,"de",pal)
#Comprovamos si hay empate.
if(j1num==j2num):
	print ("Empate")
else:
	if(j1num > j2num):
		print ("Gana jugador 1")
	else:
		print ("Gana jugador 2")
		sortir=True

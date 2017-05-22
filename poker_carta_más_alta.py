# !/bin/bash
#coding:utf-8

#Las cartas tienen un Nª: A,2-10,J,Q,K (total 13).
#Las cartas tienen un palo: picas, treboles, corazones, diamantes (total de 4).

import os
os.system('clear')
from random import randint

#Generamos la tirada de jugador 1 (coje una carta aleatoria).
j1num=randint(1,13)
#Jugador 1 coje cartas aleatorias.
if (j1num==1): 
	numero=1
if (j1num==2):
	numero=2
if (j1num==3):
	numero=3
if (j1num==4):
	numero=4
if (j1num==5):
	numero=5
if (j1num==6):
	numero=6
if (j1num==7):
	numero=7
if (j1num==8):
	numero=8
if (j1num==9):
	numero=9  
if (j1num==10):
	numero=10 
if (j1num==11):
	numero=("J")
if (j1num==12):
	numero=("Q")
if (j1num==13):
	numero=("K")
#Generamos la tirada de jugador 1 (coje una carta aleatoria).
j1pal=randint(1,4)
#Tipos de cartas de jugador 1.
if (j1pal==1):
	pal=("Picas")
if (j1pal==2):
	pal=("Diamantes")
if (j1pal==3):
	pal=("Trebol")
if (j1pal==4):
	pal=("Corazones")

print "Jugador 1 tiene un ", numero , "de" , pal

#Generamos la tirada de jugador 2 (coje una carta aleatoria).
j2num=randint(1,13)
#Jugador 2 coje cartas aleatorias.
if (j2num==1): 
	numero=1
if (j2num==2):
	numero=2
if (j2num==3):
	numero=3
if (j2num==4):
	numero=4
if (j2num==5):
	numero=5
if (j2num==6):
	numero=6
if (j2num==7):
	numero=7
if (j2num==8):
	numero=8
if (j2num==9):
	numero=9  
if (j2num==10):
	numero=10 
if (j2num==11):
	numero=("J")
if (j2num==12):
	numero=("Q")
if (j2num==13):
	numero=("K")
#Generamos la tirada de jugador 2 (coje una carta aleatoria).
j2pal=randint(1,4)
#Tipos de cartas de jugador 2.
if (j2pal==1):
	pal=("Picas")
if (j2pal==2):
	pal=("Diamantes")
if (j2pal==3):
	pal=("Trebol")
if (j2pal==4):
	pal=("Corazones") 

print "Jugador 2 tiene un ", numero , "de" , pal

#Empate
if (j1num==j2num):
	print "Empate!"
	
#Ganador
if (j1num > j2num):
	print "Gana Jugado 1!"
else:
	print "Gana Jugador 2!"

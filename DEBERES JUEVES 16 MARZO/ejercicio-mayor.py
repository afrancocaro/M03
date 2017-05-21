# !/usr/bin/python
# -*-coding: utf-8-*-

valor1=input("Indicar numero (valor):")
valor2=input("Indicar otro numero (valor):")

if valor1 == valor2:
	print ("Los numeros son iguales")
else:
	if valor1 > valor2:
			print "El numero", valor1, "es mayor"
	else:
			print "El numero", valor2, "es mayor"

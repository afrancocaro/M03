# !/usr/bin/python
# -*-coding: utf-8-*-

#Menú de una calculadora

print ("0) Salir")
print ("1) Suma")
print ("2) Resta")
print ("3) Multiplicacion")
print ("4) Division")


num = int(input("Que desea hacer el amo?\n"))
while (num >0 and num <5):
        x = int(input("Ingrese Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (num==1):
            print ("La Suma es:", x+y)
            num = int(input("Selecione Opcion\n"))
        elif(num==2):
            print ("La Resta es:",x-y)
            num = int(input("Selecione Opcion\n"))
        elif(num==3):
            print ("La Multiplicacion es:",x*y)
            num = int(input("Selecione Opcion\n"))
        elif(num==4):
            try:
              print ("La Division es:", x/y)
              num = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              num = int(input("Selecione Opcion\n"))
        if(num==0):
			print ("Adiós, hasta pronto \n")
			salir=true

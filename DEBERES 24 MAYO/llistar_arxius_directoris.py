# !/usr/bin/python
# coding:utf-8
from os import walk
import os

path_to_explore="/home/users/inf/hism1/ism47592929/Documentos/prueba"
 
# Mostrem només els arxius
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        print(name)
 
print "-------------------------------------"
# Mostrem només els directoris
for root, dirs, files in os.walk(path_to_explore):
    for name in dirs:
        print(name)
 
print "-------------------------------------"
# Mostrem tot
for root, dirs, files in os.walk(path_to_explore):
    for name in files:
        print(name)
        
    for name in dirs:
        print(name)

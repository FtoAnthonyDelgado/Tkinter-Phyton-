# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:46:04 2021

@author: USER
"""
#excepcion para que el usuario introdusca un numero en vez de una letra
#si ingresa una letra se le marcara un error que tiene que ingresar un numero
try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{} = {}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduzca bien el número")
    
#Esto sirve para ver el tipo de cualquier variable 
print(type(1))
print(type(3.14))
print(type([]))
print(type(()))
print(type({}))

#excepcion para la lectura de un archivo
def execpcion1():
    try:
        open("/home/mitocode/no_file.txt","r")
    except IOError:
        print("No existe archivo")
        
execpcion1()

#excepcion para un numero divisor de un cero
def execpcion2():
    try:
        5/0
    except ZeroDivisionError:
        print("division no permitida")
        return
execpcion2()

#Excepcion para un error de tipo de dato
def execpcion3():
    try:
        float("Micodigo")
    except ValueError:
        print("Tipo de dato no valido")
        return
    
execpcion3()
##excepcion de no encontrar un archivo 
def  execpcion4():
    try:
        open("/home/practica/excepciones","r")
    except Exception as ex:
        print(ex)
    return
execpcion4()
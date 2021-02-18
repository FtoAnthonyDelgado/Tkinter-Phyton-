# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:25:16 2021

@author: USER
"""

import os 
import time

os.mkdir("Calendario")
a=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
b=["Ejecutables","DatosUsuario","Registros"]
os.chdir("Calendario")
for elemento in a:
    os.mkdir(elemento)
    os.chdir(elemento)
    for elemento2 in b:
        os.mkdir(elemento2)
        os.chdir(elemento2)
        with open("Informe","w")as f:
            f.write(os.getcwd()+'\n')
            f.write(time.strftime('%H:%M:%S')+'\n')
            time.sleep(2)
            f.write(time.strftime('%H:%M:%S')+'\n')
            time.sleep(2)
            f.write(time.strftime('%H:%M:%S')+'\n')
        os.chdir("..")
    os.chdir("..")

    
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:34:28 2020

@author: USER
"""

import tkinter as tk
from tkinter import ttk
#######################librerias###############################################
class Vista():
    def __init__(self,ventana,modelo):
        self.model = modelo
        self.frame = tk.Frame(ventana)
        
        self.blueFrame=tk.Frame(ventana, width = 400, height = 45, bg='blue').pack()
        self.tFrame = tk.Frame(ventana, width = 400, height = 200, highlightbackground ='black' ).pack()
        self.blueFrame1 = tk.Frame(ventana, width = 400, height = 45,bg='red').pack()
        self.blueFrame2 = tk.Frame(ventana, width = 400, height = 45).pack()
        
        self.ccombo = ttk.Combobox(self.blueFrame, state = 'readonly')
        self.ccombo['values']=['cuadrado','triangulo', 'circulo','rectangulo']
        self.ccombo.bind('<<ComboboxSelected>>')
        self.cLabel2= tk.Label(self.blueFrame)
        self.cLabel3= tk.Label(self.blueFrame)
        self.cEntry2 = tk.Entry(self.blueFrame, bg= 'orange')
        
        self.ccombo.place(x =90, y=0)
        
        self.tFrameBlue= tk.Frame(self.tFrame, height = 194, width= 98, bg='blue')
        self.tFrameYellow= tk.Frame(self.tFrame, height = 194, width= 200, bg='yellow')
        self.tFrameGreen= tk.Frame(self.tFrame, height = 194, width= 97, bg='green')
        
        
        self.tFrameBlue = tk.Frame(text = "Ingrese el lado: ")
        self.valor= tk.IntVar()
        self.cEntry1= tk.Entry(self.blueFrame, textvariable= self.valor)
        
        self.cEntry1.bind('<Return>',self.area_cuadrado)
        self.cLabel2.place(x=0, y=21)
        self.cEntry1.place(x=38, y=22)
        
        self.tFrameBlue.place(x=3,y=48)
        self.tFrameYellow(x=100, y =48)
        self.tFrameGreen.place(x=300, y =48)
        
        
        def area_cuadrado(self,e):
            self.valor= int(self.cEntry1.get())
            tk.Label(self.tFrameYellow, text=self.model.area_cuadrado(self.valor)).pack()
            print(self.valor)
        
        
        
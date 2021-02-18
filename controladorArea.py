# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:22:17 2020

@author: USER
"""

import tkinter as tk
from vistaArea import Vista
from modelo import Modelo

class Controlador():
    def __init__(self):
        self.ventana = tk.Tk()
        self.modelo = Modelo()
        self.vistaArea = Vista(self.ventana,self.modelo)
        
    def inicializar(self):
        self.ventana.mainloop()
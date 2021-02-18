# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:16:03 2020

@author: USER
"""

from math import pi
class Modelo():
    ## Calculo del cuadrado
    def area_cuadrado(self, l):
        area = l*l
        return area
    ## Calculo del Triangulo
    def area_triangulo(self, b,h):
        area = (b*h)/2
        return area
    ## Calculo del Rectangulo
    def area_rectangulo(self,ba,ha):
        area = ba * ha
        return area
    ## Calculo del circulo
    def area_circulo(self,ra):
        area = pi(ra**2)
        return area

    
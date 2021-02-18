# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:34:58 2020

@author: USER
"""

import tkinter as tk

class Vista():
    def __init__(self,root):
        frame=tk.Frame(root,width=150,height=200).grid(row=0,column=0)
        self.w=tk.Canvas(root, bg='white',width=450,height=400)
        self.w.grid(row=0,column=1)
        self.legth=tk.StringVar()
        self.width=tk.StringVar()
        x=tk.Entry(frame,textvariable=self.legth)
        y=tk.Entry(frame,textvariable=self.width)
        x.place(x=10,y=40)
        y.place(x=10,y=65)
        button1=tk.Button(frame,text='Dibujar', command=self.createrec)
        button1.grid(row=0,column=0)
        
        
    def createrec(self):
        i=int(self.width.get())
        j=int(self.legth.get())
        i+=20
        j+=15
        self.w.create_rectangle(20, 15,i,j,fill='cyan')
        
class Controlador():
    def __init__(self):
        self.root = tk.Tk()
        self.view = Vista(self.root)
        
    def ejecturar(self):
        self.root.title("Graficador")
        self.root.mainloop()
        
        
if __name__=='__main__':
    c = Controlador()
    c.ejecturar()
        



        
        
    
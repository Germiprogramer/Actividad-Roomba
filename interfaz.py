#!/usr/bin/env python

#crear una interfaz grafica con tkinter

from tkinter import *
from tkinter.ttk import * 
  
class GFG: 
    def __init__(self, master = None): 
        self.master = master 

        #CORDENADAS INICIALES. 
        self.x = 1
        self.y = 0
  
        #CREAR FIGURA 
        self.canvas = Canvas(master, width = 500, height = 650) 
        #CREAR RECTANGULO
        self.rectangle = self.canvas.create_rectangle( 
                         0, 0, 50, 50, fill = "black")
        
        self.mesa = self.canvas.create_rectangle(101,220, 191,480, fill="white")
        #COLOR FONDO.
        self.canvas['bg'] = 'brown'
        
        self.canvas.pack() 
  

        #LLAMADA A LA FUNCION "movimiento"
        self.movimiento() 

    def movimiento(self):

        self.canvas.move(self.rectangle, self.x, self.y)

        self.canvas.after(100, self.movimiento)

    #MOVIMIENTO A LA IZQUIERDA
    def izquierda(self, event):
        print(event.keysym) 
        self.x = -5
        self.y = 0
      
    #MOVIMIENTO A LA DERECHA 
    def derecha(self, event):
        print(event.keysym) 
        self.x = 5
        self.y = 0
      
    #MOVIMIENTO HACIA ARRIBA 
    def arriba(self, event):
        print(event.keysym) 
        self.x = 0
        self.y = -5
      
    #MOVIMIENTO HACIA ABAJO 
    def abajo(self, event):
        print(event.keysym) 
        self.x = 0
        self.y = 5

if __name__ == "__main__": 
  
    #MOSTRAR VENTANA
    master = Tk()
    master.title("Move_tk")
    master.configure(bg="green")
    gfg = GFG(master) 

    #CONTROLAR MOVIMIENTO POR TECLADO
    master.bind("<KeyPress-Left>", lambda e: gfg.izquierda(e)) 
    master.bind("<KeyPress-Right>", lambda e: gfg.derecha(e)) 
    master.bind("<KeyPress-Up>", lambda e: gfg.arriba(e)) 
    master.bind("<KeyPress-Down>", lambda e: gfg.abajo(e)) 
    mainloop()


from Conexion import cnx
from tkinter import * 
from tkinter.ttk import *
import matplotlib.pyplot as plt

root = Tk() 
root.title("Contabilidad")
root.geometry('720x600')
root.resizable(0, 0) 
root.configure(background = "#252424")
root.columnconfigure(1, weight=1)

manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]
plt.pie(manzanas, labels=nombres)
plt.show()


mainloop() 
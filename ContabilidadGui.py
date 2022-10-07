from tkinter import * 
from tkinter.ttk import *
from Conexion import cnx
root = Tk() 

# root window title and dimension
root.title("Contabilidad")
# Set geometry(widthxheight)
root.geometry('720x600')
# Set resizable off
root.resizable(0, 0)  

root.configure(background = "#252424")
root.columnconfigure(1, weight=1)
  
sylphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\stockylogistica.png") 
conphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\contabilidad.png") 
vycphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\ventasyclientes.png")
cypphoto = PhotoImage(file = r"C:\Users\agust\OneDrive\Escritorio\Proyecto Berea\APP\App 2\Images\comprasyproveedores.png")


photoimage1 = sylphoto.subsample(2, 2)
photoimage2 = conphoto.subsample(2, 2) 
photoimage3 = vycphoto.subsample(2, 2) 
photoimage4 = cypphoto.subsample(2, 2) 
  
Button(root, text = 'Stock y Logistica', image = photoimage1, compound=TOP).grid(rowspan=2, row=0, column=0)

Button(root, text = 'Contabilidad', image = photoimage2, compound=TOP).grid(rowspan=2, row=3, column=0)

Button(root, text = 'Ventas y Clientes', image = photoimage3, compound=TOP).grid(rowspan=2, row=5, column=0)

Button(root, text = 'Compras y Proveedores', image = photoimage4, compound=TOP).grid(rowspan=2, row=7, column=0)


mainloop() 
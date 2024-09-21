import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Products import *
from Connection import *

class FormsProducts:
    
    global base 
    base = None
    
    global textBoxId
    textBoxId = None
    
    global textBoxName
    textBoxName = None
    
    global textBoxPrice
    textBoxPrice = None
    
    global textBoxDate
    textBoxDate = None
    
    global textBoxStock
    textBoxStock = None
    
    global groupBox
    groupBox = None
    
    global tree 
    tree  = None
    
    def Forms():
        global base
        global textBoxId
        global textBoxName
        global textBoxPrice
        global textBoxDate
        global textBoxStock
        global groupBox
        
    
        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Forms")
            
            groupBox = LabelFrame(base, text="Products item", padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10,pady=10)
            
            #AGRUPACIÓN DE DATOS
            
            labelId = Label(groupBox, text="Id", width=13, font=("arial", 12)).grid(row=0, column=0)
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0, column=1)
            
            
            labelName = Label(groupBox, text="Name", width=13, font=("arial", 12)).grid(row=1, column=0)
            textBoxName = Entry(groupBox)
            textBoxName.grid(row=1, column=1)
            
            labelPrice = Label(groupBox, text="Price", width=13, font=("arial", 12)).grid(row=2, column=0)
            textBoxPrice = Entry(groupBox)
            textBoxPrice.grid(row=2, column=1)
            
            labelDate = Label(groupBox, text="Date", width=13, font=("arial", 12)).grid(row=3, column=0)
            textBoxDate = Entry(groupBox)
            textBoxDate.grid(row=3, column=1)
            
            labelStock = Label(groupBox, text="Stock", width=13, font=("arial", 12)).grid(row=4, column=0)
            textBoxStock = Entry(groupBox)
            textBoxStock.grid(row=4, column=1)
            
            
            #BOTONES
            Button(groupBox, text="Save", width=10, command=saveRegister).grid(row=5, column=0)
            Button(groupBox, text="Edit", width=10).grid(row=5, column=1)
            Button(groupBox, text="Delete", width=10).grid(row=5, column=2)
            
            
            groupBox = LabelFrame(base, text="Products List", padx=5, pady=5,)
            groupBox.grid(row=0, column=1, padx=5, pady=5)
            
            #Configurating Colums
            tree = ttk.Treeview(groupBox, columns=("Id", "Name", "Price", "Date", "Stock"), show='headings', height=5,)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Id")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Name")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Price")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Date")
            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5", text="Stock")
            
            
            tree.pack()
            
            # Corregido: llamamos correctamente al método mainloop
            base.mainloop()
            
        except ValueError as error:
            print("NO FUNCIONA TU WEBADA")
            
def saveRegister():
    global textBoxName, textBoxPrice, textBoxDate, textBoxStock
    
    try:
        if textBoxName is None or textBoxPrice is None or textBoxDate is None or textBoxStock is None:
            print("Los cosos no estan inicializados") 
            return 
        
        names = textBoxName.get()
        price = textBoxPrice.get()
        date = textBoxDate.get()
        stock = textBoxStock.get()
        
        
        Products.addProducts(names, price, date, stock)
        messagebox.showinfo("Info", "Data saved")
        
        textBoxId.delete(0, END)
        textBoxName.delete(0, END)
        textBoxPrice.delete(0, END)
        textBoxDate.delete(0, END)
        textBoxStock.delete(0, END)
        
    except ValueError as error:
        print("No funciona mi chamo".format(error))
            
FormsProducts.Forms()
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Products import *
from Connection import *

class FormsProducts:
    def Forms():
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
            Button(groupBox, text="Save", width=10).grid(row=5, column=0)
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
            
            
            
            
            
            
            # Corregido: llamamos correctamente al método mainloop
            base.mainloop()
            
        except ValueError as error:
            print("NO FUNCIONA TU WEBADA")
            
FormsProducts.Forms()
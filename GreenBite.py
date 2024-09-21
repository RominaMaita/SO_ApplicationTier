import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FormsProducts:
    def Forms():
        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Forms")
            
            groupBox = LabelFrame(base, text="Products item", padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10,pady=10)
            
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
            
            Button(groupBox, text="Save", width=10).grid(row=5, column=0)
            Button(groupBox, text="Edit", width=10).grid(row=5, column=1)
            Button(groupBox, text="Delete", width=10).grid(row=5, column=2)
            
            
            
            
            # Corregido: llamamos correctamente al método mainloop
            base.mainloop()
            
        except ValueError as error:
            print("NO FUNCIONA TU WEBADA")
            
FormsProducts.Forms()

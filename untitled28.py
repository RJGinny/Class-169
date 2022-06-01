#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:09:44 2022

@author: riddhiekajain
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createNewElement(self):
        label = Label(root, text = "A new label has been created using class", fg="red")
        label.pack()
        btn = Button(root, text =" Button", command = self.message)
        btn.pack(padx=20, pady = 10)
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text ="Click to create label and button element", command= 
obj_of_CreateElements.createNewElement)
btn.pack(padx=20, pady= 10)

root.mainloop()
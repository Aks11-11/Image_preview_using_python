from tkinter import filedialog, BOTTOM
import tkinter as tk
from tkinter.filedialog import Open
from PIL import Image, ImageTk
import os
from setuptools import setup

def showimage(self=None):
    filedialog.askopenfile(initialdir=os.getcwd(), title="Select image file",
                           filetype=(("JPG File", "*.jpg"), ("PNG File", "*png"), ("All file", "how are oyu.txt")))
    from django.contrib.admin import options
    filename = Open(**options).show()
    img = Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.config(image=img)
    lbl.iamge = img

with open("/Users/akshat/Desktop/icons/dog.png") as f:
    long_description = f.read()

root = tk.Tk()

fram  = tk.Frame(root)
fram.pack(side=BOTTOM,padx=15,pady=15)

lbl = tk.Label(root)
lbl.pack()

btn = tk.Button(fram, text="Select image", command=showimage)
btn.pack(side=tk.LEFT)

btn2 = tk.Button(fram,text="Exit",command=lambda:exit())
btn2.pack(side=tk.LEFT,padx=12)

root.title("Ak's Previewer")
root.geometry("500x500")
root.mainloop()

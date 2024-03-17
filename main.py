from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
def showimage():
    filename = filedialog.askopenfile(initialdir=os.getcwd(),title="Select image file",filetype=(("JPG File","*.jpg"),("PNG File","*png"),("All file","how are oyu.txt")))
    img = Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.config(image=img)
    lbl.image = img

root = Tk()

fram  = Frame(root)
fram.pack(side=BOTTOM,padx=15,pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(fram,text="Select image",command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(fram,text="Exit",command=lambda:exit())
btn2.pack(side=tk.LEFT,padx=12)

root.title("Ak's Previewer")
root.geometry("500x500")
root.mainloop()

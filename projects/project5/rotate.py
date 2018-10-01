#!/usr/bin/env python3
# Michael Gates
# 8 October 2018
# Rotates images via GUI controls

import os
import PIL.Image
from tkinter import filedialog
from tkinter import *


tk = Tk()
tk.title("Image Rotator")

def doFileOpen(pathEntry):
    tk.filename = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    pathEntry.insert(0, tk.filename)
    print("Selected: " + tk.filename)

def rotatecw90():
    if not tk.filename:
        print("No image selected!")
        return
    img = PIL.Image.open(tk.filename)
    newImg = img.rotate(-90)
    newImg.show()
    print("Showing image rotated CW 90 degrees")
    newImg.save(tk.filename.replace(".jpg","") + "-rotated-cw-90.jpg")
    print("Saving image rotated CW 90 degrees")

def rotateccw90():
    if not tk.filename:
        print("No image selected!")
        return
    img = PIL.Image.open(tk.filename)
    newImg = img.rotate(90)
    newImg.show()
    print("Showing image rotated CCW 90 degrees")
    newImg.save(tk.filename.replace(".jpg","") + "-rotated-ccw-90.jpg")
    print("Saving image rotated CCW 90 degrees")

"""
MAIN PROGRAM FUNCTION
"""
def main():

    f = Frame(tk, width=200, height=200)
    f.pack()

    label = Label(f, text="File Path")
    label.pack()

    pathEntry = Entry(f)
    pathEntry.pack()

    close_button = Button(f, text="Close", command=tk.quit)
    close_button.pack()

    menubar = Menu(tk)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=lambda: doFileOpen(pathEntry))
    filemenu.add_command(label="Rotate 90 Degrees CW", command=lambda: rotatecw90())
    filemenu.add_command(label="Rotate 90 Degrees CCW", command=lambda: rotateccw90())
    menubar.add_cascade(label="File", menu=filemenu)

    tk.config(menu=menubar)

    tk.mainloop()

if __name__ == '__main__':
    main()

#!/bin/python3

from tkinter import *
from tkinter import filedialog
from tkinter import font
import os

root = Tk()
root.title('TxtEd')
#root.iconbitmap('')
root.geometry('900x560')

global openStatusName
openStatusName = False

def newFile():
    global openStatusName
    openStatusName = False
    mytext.delete('1.0', END)
    root.title('*untitled')

def openFile():
    mytext.delete('1.0', END)
    textFile = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open File',
        filetypes=(("Text Files", '*.txt'), ("HTML", '*.html'),
                    ("Python", '*.py'), ("C", '*.c'), ("C++", '*.cpp'), ("All Files", '*.*')))
    
    if textFile:
        global openStatusName
        openStatusName = textFile

    name = textFile
    root.title("{}".format(name))
    textFile = open(textFile, 'r')
    stuff = textFile.read()
    mytext.insert(END, stuff)
    textFile.close()

def saveAsFile():
    textFile = filedialog.asksaveasfilename(defaultextension='.*', initialdir=os.getcwd(), title='Save File',
        filetypes=(("All Files", '*.*'), ("HTML", '*.html'),
                    ("Python", '*.py'), ("C", '*.c'), ("C++", '*.cpp'), ("Text Files", '*.txt')))
    if textFile:
        name = textFile
        root.title("{}".format(name))
        textFile = open(textFile, 'w')
        textFile.write(mytext.get(1.0, END))
        textFile.close()

def saveFile():
    global openStatusName
    if openStatusName:
        textFile = open(openStatusName, 'w')
        textFile.write(mytext.get(1.0, END))
        textFile.close()

    else:
        saveAsFile()

frame = Frame(root)
frame.pack(pady=7)

textScroll = Scrollbar(frame)
textScroll.pack(side=RIGHT, fill=Y)
sideScroll = Scrollbar(frame, orient='horizontal')
sideScroll.pack(side=BOTTOM, fill=X)

mytext = Text(frame, width=105, height=50, font=('Droid Sans Mono', 13),
    selectbackground='grey', selectforeground='black', undo=True, wrap='none',
    yscrollcommand=textScroll.set, xscrollcommand=sideScroll.set
)
mytext.pack()

textScroll.config(command=mytext.yview)
sideScroll.config(command=mytext.xview)

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=newFile)
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_command(label='Save As', command=saveAsFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)

#editMenu = Menu(menu, tearoff=False)
#menu.add_cascade(label='Edit', menu=editMenu)
#editMenu.add_command(label='Cut')
#editMenu.add_command(label='Copy')
#editMenu.add_command(label='Undo')
#editMenu.add_command(label='Redo')

#statusBar = Label(root, text='Ready  ', anchor=E)
#statusBar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()



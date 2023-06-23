import tkinter as tk
from functools import partial
import pathlib
from tkinter import ttk
import os
#from tkinter import *
'''
TODO:
- Store all selected pdf to a list 
- print all selected pdf
- if possible, make a preview window on left side of the soft
- Specific button for open the pdf

'''


root = tk.Tk()
root.title("PDF Printer V 1.0")
root.geometry("400x350")
root.resizable(False, False)


folderPath = tk.StringVar(value=r"Enter Folder Path")



def on_button_click():
    #print(folderPath.get())
    global pdfListDict
    pdfListDict = {}
    for p in pathlib.Path(folderPath.get()).iterdir():
        if p.is_file() and (str(p).endswith(".pdf") or str(p).endswith(".PDF")):
            #print(p.name)
            pdfListDict.update({p.name:p})
            
    #print(pdfList)
    listbox.delete('0',tk.END)
    for f,d in pdfListDict.items():
        listbox.insert(tk.END, f)


def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    fileName = ",".join([listbox.get(i) for i in selected_indices])
    global j
    j = fileName.split(",")
    #print(type(j))
    #print(j)


def printAll():
    for k in j:
        print(pdfListDict[k])

def openPDF():
    print("Open", pdfListDict[listbox.get(listbox.curselection())])
    os.startfile(pdfListDict[listbox.get(listbox.curselection())])

pdfList = []

listBoxVar = tk.Variable(value=pdfList)

path = tk.Entry(root,  textvariable= folderPath, width= 35)

path.grid(row=0, column=0, columnspan=3, pady= 20, padx=20 )
path.focus()


button = tk.Button(root, text="Get All PDFs", command=on_button_click)
button.grid(row=0, column=3, sticky= (tk.W))

listbox = tk.Listbox(root, listvariable= listBoxVar, selectmode= tk.EXTENDED, height= 10, width=50)
listbox.grid(row=2, column=0, columnspan=4, rowspan=4, padx = 20)

printAllpdf = tk.Button(root, text="Print All", command= printAll)
printAllpdf.grid(row=6, column=0, columnspan=2, pady=20)

open = tk.Button(root, text="Open File", command= openPDF)
open.grid(row=6, column=2, columnspan=2 , pady=20)



scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.grid(row=2, column=4, rowspan=4,)

listbox.bind('<<ListboxSelect>>', items_selected)

madeBy = tk.Label(root, text="Developed by r Patel with 💙 !!")
madeBy.grid(row=7, column=0, columnspan=4, pady=5)

root.mainloop()




    

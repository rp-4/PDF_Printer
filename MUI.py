import customtkinter
from CTkListbox import *
'''
TODO:
- Store all selected pdf to a list 
- print all selected pdf
- if possible, make a preview window on left side of the soft
- Specific button for open the pdf

'''

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("500x420")
app.title("PDF Printer v 1.0.0")
app.resizable(False, False)
app.grid_columnconfigure(0, weight=1)

#folderPath = tk.StringVar(value=r"Enter Folder Path")

def on_button_click():
    #print(folderPath.get())
    print("Get em all")
    '''global pdfListDict
    pdfListDict = {}
    for p in pathlib.Path(folderPath.get()).iterdir():
        if p.is_file() and (str(p).endswith(".pdf") or str(p).endswith(".PDF")):
            #print(p.name)
            pdfListDict.update({p.name:p})'''


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(row=0, column=0, padx=20, pady=20, sticky = "news")
'''
entr_lbl = customtkinter.CTkLabel(master=frame_1, text="Enter the folder path", justify=customtkinter.LEFT)
entr_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")'''

entr_fldr = customtkinter.CTkEntry(master=frame_1, placeholder_text="Enter the folder path", width= 345)
entr_fldr.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="we")

get_all = customtkinter.CTkButton(master=frame_1, text="Get All PDFs", command=on_button_click, width=60)
get_all.grid(row=0, column=3, sticky= "w")

listbox = CTkListbox(master=frame_1,multiple_selection = True, height= 10, )
listbox.grid(row=1, column=0, columnspan=4,padx=10, pady=10, sticky= "we")

listbox.insert(0, "Option 0")
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.insert(3, "Option 3")
listbox.insert(4, "Option 4")
listbox.insert(5, "Option 5")
listbox.insert(6, "Option 6")
listbox.insert(7, "Option 7")
listbox.insert("END", "Option 8")

print_choice = customtkinter.CTkSegmentedButton(master=frame_1, values=["Print Selected", "Print All"])
print_choice.grid(row=2, column=0, columnspan=1,padx=10, pady=10, sticky= "we")

print_now = customtkinter.CTkButton(master=frame_1, text="Print", command=on_button_click, width=80)
print_now.grid(row=2, column=1, padx=5, sticky= "e")

open_pdf = customtkinter.CTkButton(master=frame_1, text="Open", command=on_button_click, width=80)
open_pdf.grid(row=2, column=3, padx=5, sticky= "w")




madeBy = customtkinter.CTkLabel(master=app, text="Developed by r Patel with 💙 !!")
madeBy.grid(row=3, column=0, columnspan=4, pady=0)

app.mainloop()

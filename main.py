import pandas as pd
import pyautogui
import openpyxl
import xlrd
import time
import os
import sys
#import win32print 
import pathlib
#from pywintypes import com_error
import pdf2image
from pdf2image import convert_from_path
import numpy as np
import subprocess
import os.path
import PyPDF2





st = time.time()

###########################

def main():
    
    allPrinters = [r"BnW Printer",r"Color Printer"]
    
    '''for printer in allPrinters:
        checkPrinter(printer)'''
        
    #ask for folder location
    path = input("Enter folder Path: ").strip()
    
    env = input("Test = 0 and Print = 1 :").strip()
    
    if env == "0":
        t = "0"
    elif env == "1":
        t = "1"
        
    pdfs = getAllPdfUrls(path)
    for p in pdfs:
        print("\nPrinting==========: "+str(p).rsplit("\\",1)[-1]+"\n")
        ans = input("Want to print, 1 for Yes & 0 for No, x to cancel :")
        if ans == "1":
            checkPDFpageColor(p, t)
        elif ans == "x":
            sys.exit("Thank you for using the script, see you nest time !!")
        
    
    
'''    
def checkPrinter(printer_name):
    try:
        handle = win32print.OpenPrinter(printer_name)   
        #print(handle)
    except: 
        sys.exit(f"Printer {printer_name} is not available.")'''
        
        
def getAllPdfUrls(path):
    
    #return all full url of pdf files except VC
    all_PDFs = []
    d = pathlib.Path(path)
    try:
        for i in d.iterdir():
            if i.is_file() and str(i).count("-VC") > 1:
                #print("VC")
                pass
            elif i.is_file() and str(i).endswith(".pdf") and len(str(i).rsplit("\\",1)[-1]) < 9:
                #print(len(str(i).rsplit("\\",1)[-1]))
                pass
            elif i.is_file() and (str(i).endswith(".PDF") or str(i).endswith(".pdf")) and len(str(i).rsplit("\\",1)[-1]) > 5:
                #print(i)
                #print(len(str(i).rsplit("\\",1)[-1]))
                all_PDFs.append(i)
    except:    
        sys.exit("No single pdf found.")
    
    #print(all_PDFs)
    return all_PDFs
                

def checkPDFpageColor(path, envmnt):
    print("==============================================")
    #print(path)
    images = convert_from_path(path,poppler_path=r'Path to \poppler-23.05.0\Library\bin')
    
    p = 1
    npg = []
    cpg = []
    normalPagesToPrint = {}
    colorPagesToPrint = {}
    
    #variable for printers to use in dict
    test = "Microsoft Print to PDF"
    if envmnt == "0":
        color = test
        normal = test
    elif envmnt == "1":
        color = "color printer name"
        normal = "BnW printer name"
    
    
    for image in images:
        img = np.array(image.convert('HSV'))
        hsv_sum = img.sum(0).sum(0)
        if hsv_sum[0] == 0 and hsv_sum[1] == 0:
            #print(p, "====== Normal")
            #printSinglePage(path, "default", p, "Microsoft Print to PDF")
            #printSinglePage(path, "default", p, "BnW printer name")
            npg.append(p)
            p += 1
        else:
            #print(p, "====== Color")
            #printSinglePage(path,"default", p, "Microsoft Print to PDF")
            #printSinglePage(path,"default", p, "color printer name")
            cpg.append(p)
            p += 1
    #print(npg)
    normalPagesToPrint.update({"Path":f"{path}",
        "Pages": npg,
        "Printer": normal})
    #print(normalPagesToPrint)
    #print(cpg)
    colorPagesToPrint.update({"Path":f"{path}",
        "Pages": cpg,
        "Printer": color})
    #print(colorPagesToPrint)
    
    if normalPagesToPrint["Pages"]:
        printWholePDF(normalPagesToPrint["Path"], "default", str(normalPagesToPrint["Pages"])[1:-1], normalPagesToPrint["Printer"])
    if colorPagesToPrint["Pages"]:
        printWholePDF(colorPagesToPrint["Path"], "default", str(colorPagesToPrint["Pages"])[1:-1], colorPagesToPrint["Printer"])
    

#optional function to ask for printer and save in a file which can be used to read printer name

def askForPrinterName():
    color = input("Enter Color Printer Name: ").strip()
    BnW = input("Enter Black n White Printer Name: ").strip()

    contents = [ color,  BnW]
    with open("0.txt", "w+") as file:
        for i in contents:
            file.write(str(i)+"\n")
        
        
def printWholePDF(fileURL, orientation, pg, printerColor):
    
    sumatra = "Path to \\SumatraPDF-3.4.6-64.exe"
    
    # opened file as reading (r) in binary (b) mode
    file = open(fileURL, 'rb')

    # store data in pdfReader
    pdfReader = PyPDF2.PdfReader(file)

    # count number of pages
    totalPages = len(pdfReader.pages)

    # print number of pages
    print(f"Total Pages: {totalPages}")
        
    
    #p = [1,3]
    
    pageList = str(pg)
    
    pages = f"{orientation}, {pageList},1x"
            
  #try to print the pdf and if doesnt work then give error
    try:
        
        subprocess.call([sumatra, '-print-to', printerColor, '-print-settings', pages, fileURL])

    except BaseException as msg:
        print(msg)
        

if __name__ == "__main__":
    main()



####################################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

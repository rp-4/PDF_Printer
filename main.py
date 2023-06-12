import pandas as pd
import pyautogui
import openpyxl
import xlrd
import time
import os
import sys
import win32print 
import pathlib
from pywintypes import com_error
import pdf2image
from pdf2image import convert_from_path
import numpy as np
import subprocess
import os.path
import PyPDF2





st = time.time()

###########################

def main():
    
    allPrinters = [r"Brother HL-L5200DW series PrintEr",r"HP Color LaserJet Pro M478f-9f [D39EC8]"]
    
    for printer in allPrinters:
        checkPrinter(printer)
        
    #ask for folder location
    path = input("Enter folder Path: ").strip()
    
    pdfs = getAllPdfUrls(path)
    for p in pdfs:
        checkPDFpageColor(p)
        
    
    
    
def checkPrinter(printer_name):
    try:
        handle = win32print.OpenPrinter(printer_name)   
        #print(handle)
    except: 
        sys.exit(f"Printer {printer_name} is not available.")
        
        
def getAllPdfUrls(path):
    
    #return all full url of pdf files except VC
    all_PDFs = []
    d = pathlib.Path(path)
    for i in d.iterdir():
        if i.is_file() and str(i).endswith("-VC.PDF"):
            #print("VC")
            pass
        elif i.is_file() and str(i).endswith(".PDF"):
            print(i)
            all_PDFs.append(i)
    
    #print(all_PDFs)
    return all_PDFs
                

def checkPDFpageColor(path):
    print("==============================================")
    print(path)
    images = convert_from_path(path,poppler_path=r'C:\Users\Iconic\Downloads\python\poppler-23.05.0\Library\bin')
    
    p = 1
    npg = []
    cpg = []
    for image in images:
        img = np.array(image.convert('HSV'))
        hsv_sum = img.sum(0).sum(0)
        if hsv_sum[0] == 0 and hsv_sum[1] == 0:
            print(p, "====== Normal")
            npg.append(p)
            p += 1
        else:
            print(p, "====== Color")
            cpg.append(p)
            p += 1
    print(npg)
    print(cpg)

def askForPrinterName():
    color = input("Enter Color Printer Name: ").strip()
    BnW = input("Enter Black n White Printer Name: ").strip()

    contents = [ color,  BnW]
    with open("0.txt", "w+") as file:
        for i in contents:
            file.write(str(i)+"\n")
            

def printIt(fileURL, printerColor):
    
    sumatra = "C:\\Users\\Iconic\\Downloads\\SumatraPDF-3.4.6-64\\SumatraPDF-3.4.6-64.exe"
    
    # opened file as reading (r) in binary (b) mode
    file = open(fileURL, 'rb')

    # store data in pdfReader
    pdfReader = PyPDF2.PdfReader(file)

    # count number of pages
    totalPages = len(pdfReader.pages)

    # print number of pages
    print(f"Total Pages: {totalPages}")
        
    
    p = [1,3]
    
    pageList = str(p)[1:-1]
    
    pages = f"portrait, {pageList},1x"
            
  #try to print the pdf and if doesnt work then give error
    try:
        
        subprocess.call([sumatra, '-print-to', "Microsoft Print to PDF", '-print-settings', pages, pdf_name])

    except BaseException as msg:
        print(msg)
        

if __name__ == "__main__":
    main()



####################################

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

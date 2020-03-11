import os,zipfile,sys
from PIL import Image
import re
import time
from tqdm import tqdm
# I found this function in stackoverflow. It is a sorting algorithm. OS sorts files like this 1,10,...,2,20,...,3 etc.
# This function solves that. Thanks to user user136036
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def userInput(name:str):
    a=input(f"{name}..:")
    return a

def conPDF(basepath):
    liste=[]
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            liste.append(entry)
    for direc in tqdm(liste):
        newpath=f"{basepath}/{direc}"
        imglist=[]
        for entry in sorted_alphanumeric(os.listdir(newpath)):
            if os.path.isfile(os.path.join(newpath, entry)):
                path=f'{newpath}/{entry}'
                images=Image.open(r"{}".format(path))
                pdf=images.convert('RGB')
                imglist.append(pdf)
        pdf=imglist[0]
        imglist.pop(0)
        pdf.save(r'{}/{}.pdf'.format(basepath,direc),quality=100,save_all=True, append_images=imglist)

def conCBZ(basepath):
    liste=[]
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            liste.append(entry)
    for direc in tqdm(liste):
        newpath=f"{basepath}/{direc}"
        cbz=newpath+'.cbz'
        z=zipfile.ZipFile(cbz,'w')
        for entry in sorted_alphanumeric(os.listdir(newpath)):
            if os.path.isfile(os.path.join(newpath, entry)):
                path=f'{newpath}/{entry}'
                z.write(path)
        z.close()

def main():
    basepath=userInput("Directory")
    filetype=userInput("C for CBZ, P for PDF \nWhich Type..:").upper()
    if filetype=="C":
        conCBZ(basepath)
    else:
        conPDF(basepath)

if __name__ == "__main__":
    main()
        
# -----------------------------------------------------------	
# Converts images to pdf or cbz
# (C) 2020 Ercan Berber, Istanbul, Turkey	
# Released under MIT License
# -----------------------------------------------------------

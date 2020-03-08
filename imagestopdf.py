import os
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

# Gets location of a root from user and returns it.
def dirInput():
    a=input("Directory..:")
    return a

# @basepath; location from user
# returns the folders
def lookforDir(basepath):
    liste=[]
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            liste.append(entry)
    return liste

# @basepath; location from user
# @liste; list of a folders inside the root.
def openDir(liste,basepath):
    for direc in tqdm(liste):
        newpath=f"{basepath}/{direc}"
        scanfile(newpath,basepath,direc)

# @newpath; basepath+folder name
# @basepath; location from user
# @direc; folder name
def scanfile(newpath,basepath,direc):
    imglist=[]
    for entry in sorted_alphanumeric(os.listdir(newpath)):
        if os.path.isfile(os.path.join(newpath, entry)):
            path=f'{newpath}/{entry}'
            images=Image.open(r"{}".format(path))
            pdf=images.convert('RGB')
            imglist.append(pdf)
    convertToPDF(imglist,basepath,direc)

# @imglist; list of a image
# @basepath; location from user
# @direc; folder name
def convertToPDF(imglist,basepath,direc):
    pdf=imglist[0]
    imglist.pop(0)
    pdf.save(r'{}/{}.pdf'.format(basepath,direc),save_all=True, append_images=imglist)
    #saves the file as folder_name.pdf insede the root.

def main():
    basepath=dirInput()
    liste=lookforDir(basepath)
    openDir(liste,basepath)

if __name__ == "__main__":
    main()

# -----------------------------------------------------------	
# Converts images to pdf
# (C) 2020 Ercan Berber, Istanbul, Turkey	
# Released under MIT License
# -----------------------------------------------------------

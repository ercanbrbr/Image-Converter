import os
from PIL import Image
import re
# I found this function in stackoverflow. It is a sorting algorithm. OS sorts files like this 1,10,...,2,20,...,3 etc.
# This function solves that. Thanks to user user136036
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def dirInput():
    print("Copy paste the directory but change '\\' to '/' ")
    a=input("Directory..:")
    return a

def lookforDir(basepath):
    liste=[]
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            liste.append(entry)
    return liste

def openDir(liste,basepath):
    for direc in liste:
        newpath=f"{basepath}/{direc}"
        scanfile(newpath,basepath,direc)

def scanfile(newpath,basepath,direc):
    imglist=[]
    for entry in sorted_alphanumeric(os.listdir(newpath)):
        if os.path.isfile(os.path.join(newpath, entry)):
            path=f'{newpath}/{entry}'
            images=Image.open(r"{}".format(path))
            pdf=images.convert('RGB')
            imglist.append(pdf)
    convertToPDF(imglist,basepath,direc)

def convertToPDF(imglist,basepath,direc):
    pdf=imglist[0]
    imglist.pop(0)
    pdf.save(r'{}/{}.pdf'.format(basepath,direc),save_all=True, append_images=imglist)

def main():
    basepath=dirInput()
    liste=lookforDir(basepath)
    openDir(liste,basepath)

if __name__ == "__main__":
    main()

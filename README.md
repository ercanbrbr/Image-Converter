# Image-Converter

I made this tool to convert manga files that I downloaded to pdf/cbz. You can use this tool to convert any image (jpg,jpeg,png) to pdf/cbz file. I didn't try other type of files but It supports tiff, bmp and gif according to the documentation from the library that I used.

Bu programı indirdiğim manga dosyalarını pdf/cbz'ye çevirmek için yazdım. Herhangi bir resim dosyasını (jpg,jpeg,png) pdf/cbz'ye çevirmek için kullanabilirsiniz. Başka dosya türleri denemedim ama kullandığım kütüphanenin dokümentasyonuna göre tiff, bmp ve gif destekliyor. 

# How to Use

Put the files in a folder. Folder should only contains image file. Put that folder in a root folder. Root folder can contain another files, and folder if you want that folder to be converted as well. Copy the location of the root folder. Run the tool and paste the location.

Resimleri bir klasörün içine atın. Klasörün sadece resim dosyası içermeli. 
O klasörü de bir kökün içine atın. Kökün içinde başka dosyalar olabilir, ve eğer dönüştürülmesini istiyorsan başka bir dosya daha içerebilir.
Kök klasörünün konumunu kopyalayın. Programı çalıştırıp uzantıyı yapıştırın.

A picture explanining how it works.

Çalışma mantığını anlatan bir resim.

Before | After
------------ | -------------
![example](https://i.imgur.com/E4clUf0.png) | ![RESULT](https://i.imgur.com/lvsfmqy.png)

Program girdi çıktı

Input | Output
------------ | -------------
![example](https://i.imgur.com/N3MJniC.png) | ![RESULT](https://i.imgur.com/QOBiOCx.png)

# Requirements 
 
Pillow

```
pip install Pillow
```
tqdm

```
pip install tqdm
```

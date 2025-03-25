# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 17:30:18 2025

@author: seyma
"""
import pandas as pd
sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
         "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
         "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}
##### 1. Yukarıdaki sözlüğü bir DataFrame haline getirin.
data = pd.DataFrame(sozluk)
print(data,"\n","\n")

##### 2. Aşağıdaki işlemleri dataframe üzerinde uygulayalım.
#- Giyim kategorisinde bulunan ürünleri gösterin
print(data[data["Kategori"]=="Giyim"]["Ürün"],"\n","\n")
#- Ayakkabı kategorisinde bulunan ürünleri gösterin
print(data[data["Kategori"]=="Ayakkabı"]["Ürün"],"\n","\n" )
#- Aksesuar kategorisinde bulunan ürünleri gösterin
print(data[data["Kategori"]=="Aksesuar"]["Ürün"],"\n","\n")


##### 3 Aşağıdaki işlemleri dataframe üzerinde uygulayalım.
#- Giyim kategorisinde fiyatı 300'den fazla olan ürünleri gösterin
print(data[(data["Kategori"] =="Giyim") & (data["Fiyat"]>300)],"\n","\n")
#- Ayakkabı kategorisinde fiyatı 600'den az olan ürünleri gösterin
print(data[(data["Kategori"] =="Ayakkabı") & (data["Fiyat"]>600)],"\n","\n")
#- Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuarı gösterin
print(data[(data["Kategori"] =="Aksesuar") & (data["Fiyat"]>100)],"\n","\n")


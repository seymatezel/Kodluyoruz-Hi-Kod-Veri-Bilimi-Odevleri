# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 15:12:42 2025

@author: seyma
"""

# x = 3  floata çevirelim. Çevirdikten sonra veri tipinide yazdıralım.
x=3 
x_2=float(x)
print(type(x_2))

#y = 4.5 -----> integere çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
y=4.5
y_2=int(y)
print(type(y_2))

#z = 8 -----> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
z=8
z_2=int(z)
print(type(z_2))

#a =12 -----> floata çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
a=12
a_2=float(a)
print(type(a_2))

#b = 46.8 ------> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
b=46.8
b_2=int(b)
print(type(b_2))

#İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. Bu karşılaştırmalara mantıksal operatörler de eklenir.
burcu=19
kubra=21
zeynep=18
print(burcu==kubra)
print(zeynep<burcu)
print(zeynep>kubra)
print(burcu==kubra and zeynep<burcu )
print(zeynep>kubra or zeynep<burcu)
print(not burcu==kubra)


#Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.
sayi_1=int(input("ilk sayı:"))
sayi_2=int(input("ikinci sayı:"))
print(sayi_1+sayi_2)
print(sayi_1-sayi_2)
print(sayi_1*sayi_2)
print(sayi_1/sayi_2)

#Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.
isim=input("isminizi giriniz:")
yas=int(input("yaşınızı giriniz:"))
sehir=input("yaşadığınız şehir:")
meslek=input("mesleğiniz:")
print(isim, yas, sehir, meslek)

#Hi-Kod Veri Bilimi Atölyesi ifadesini bir değişkene tanımlanır.
# 1. İfadedeki her bir kelimeyi (\"Hi-Kod\", \"Veri\", \"Bilimi\", \"Atölyesi\") değişken içinden seçilir.
#2. İfadeyi hepsini büyük harf olacak hale çevrilir. (\"HI-KOD VERİ BİLİMİ ATÖLYESİ\")
#3. İfadeyi hepsini büyük harf olacak hale çevrilir.(\"hi-kod veri bilimi atölyesi\")
degisken="Hi-Kod Veri Bilimi Atölyesi"

ikinci= degisken.upper()
ucuncu=degisken.lower()
print(ikinci)
print(ucuncu)

#0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir.("02468", "13579")
sayi="0123456789"
cift_sayilar = sayi[::2]
tek_sayilar = sayi[1::2]
print(str(cift_sayilar))
print(str(tek_sayilar))

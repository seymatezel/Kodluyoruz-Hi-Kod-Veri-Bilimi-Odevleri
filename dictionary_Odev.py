# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 20:54:10 2025

@author: seyma
"""

# Ödev 1
#Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur. Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.

"""ogrenci_notlari = {
    "Ali": {"Matematik": 50, "Fizik": 60, "Kimya": 70},
    "Ayşe": {"Matematik": 85, "Fizik": 80, "Kimya": 50},
    "Mehmet": {"Matematik": 40, "Fizik": 60, "Kimya": 55},
    "Zeynep": {"Matematik": 70, "Fizik": 70, "Kimya": 75},
    "Zehra": {"Matematik":90, "Fizik":75, "Kimya": 95},
}

isim=input("İsminiz nedir?:")
print(isim, ":" , ogrenci_notlari[isim])"""


#Ödev 2
#Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.

"""ogrenci_notlari = {
    "Ali": {"Matematik": 50, "Fizik": 60, "Kimya": 70},
    "Ayşe": {"Matematik": 85, "Fizik": 80, "Kimya": 50},
    "Mehmet": {"Matematik": 60, "Fizik": 60, "Kimya": 55},
    "Zeynep": {"Matematik": 70, "Fizik": 70, "Kimya": 75},
    "Zehra": {"Matematik":90, "Fizik":75, "Kimya": 95},
}

ogrenci_notlari["Mehmet"]["Matematik"]=65
print(ogrenci_notlari)

ogrenci_notlari["Ahmet"]={"Matematik":100,"Fizik":95,"Kimya":50}
print(ogrenci_notlari)

isim = input("Matematik notunu öğrenmek istediğiniz öğrencinin adını girin: ")
if isim in ogrenci_notlari:
    if "Matematik" in ogrenci_notlari[isim]:
        matematik_notu = ogrenci_notlari[isim]["Matematik"]
        print(matematik_notu)
else:
    print(f"{isim} adında bir öğrenci bulunmuyor.")
          
          

matematik_50_alanlar = []

for isim, notlar in ogrenci_notlari.items():
    if "Matematik" in notlar and notlar["Matematik"] == 50:
        matematik_50_alanlar.append(isim)
print(matematik_50_alanlar)"""



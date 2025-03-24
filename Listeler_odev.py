# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 20:28:56 2025

@author: seyma
"""

#Odev-1
"""liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

#1. Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.
   # - "3" değerine ulaşmak için indexleme yapın.
print(liste.index("3"))
   #- "Hi-Kod" değerine ulaşmak için indexleme yapın.
print(liste.index("Hi-Kod"))
   #- 4.7 değerine ulaşmak için indexleme yapın.
print(liste.index(4.7))
   #- 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
print(liste[2:6])
   #- 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
print(liste[4:6],liste[6:8]) """  


#Odev-2
#Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

"""liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
yeni_liste=[]
for eleman in liste:
    if type(eleman) is str:
        yeni_liste.append(eleman)
print(yeni_liste)"""


#Odev-3
#Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.

"""meyveler = ["elma", "armut", "çilek", "muz", "kivi"]
#Enumarete(index, listedeki eleman) şeklinde kullanılır.
for index, meyve in enumerate(meyveler):
    print(f"{index}. indexte bulunan meyve: {meyve}")"""
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 21:39:46 2025

@author: seyma
"""
import numpy as np
#1.Sayılardan oluşan bir boyutlu array oluşturun.
#Oluşturulan arrayin boyut, eleman sayısı bilgilerine bakalım.

"""array=np.array([12,18,13,25,19])
print("Array boyutu:", array.ndim) #,ndim arrayın boyutunu çıktı olarak veriyor.
print("Eleman Sayısı:",array.size)"""



# 2. Aşağıda verilen iki boyutlu ve üç boyutlu arrayi oluşturalım.

"""İki_boyutlu_array= np.array([[1,2,6,7],[4,3,9,5]])

Üç_boyutlu_array=np.array([[[7,5,14],[21,8,11]],[[8,6,20],[14,3,9]]])


# İstenilen elamanlara ulaşmak için arrayler üzerinde indexleme işlemi yapalım
#İki boyutlu arraydaki 2 elemanına ulaşalım
print(İki_boyutlu_array[0,1])
#İki boyutlu arraydaki 7 elemanına ulaşalım
print(İki_boyutlu_array[0,3])
#Üç boyutlu arraydaki 9 elemanına ulaşalım
print(Üç_boyutlu_array[1,1,2])
#Üç boyutlu arraydaki 5 elemanına ulaşalım
print(Üç_boyutlu_array[0,0,1])

#Arrayler üzerinde slicing işlemi uygulayalım.
#İki boyutlu arraydaki 2,6 elemanlarına ulaşalım
print(İki_boyutlu_array[0:1,1:3])
#İki boyutlu arraydaki 3,9,5 elemanlarına ulaşalım
print(İki_boyutlu_array[1:2,1:4])
#Üç boyutlu arraydaki 21,8,11 elemanlarına ulaşalım
print(Üç_boyutlu_array[0:1,1:2,0:])
#Üç boyutlu arraydaki 6,20 elemanlarına ulaşalım
print(Üç_boyutlu_array[1:2,0:1,1:3])"""
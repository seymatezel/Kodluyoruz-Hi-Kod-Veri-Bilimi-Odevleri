# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 18:59:32 2025

@author: seyma
"""

#1.Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

"""def daire_alani():
    pi_degeri=float(input("Pi değerini giriniz:"))
    yaricap=float(input("Yarıçapı giriniz:"))
    alan=pi_degeri*(yaricap**2)
    print(alan)
daire_alani()"""

#2.Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. Format metodunu kullanılarak ekrana yazdırılır.

"""def faktoriyel(sayi):
    if sayi < 0:
        print("Negatif sayıların faktöriyeli hesaplanamaz.")
        return
    elif sayi == 0 or sayi == 1:
        sonuc = 1
    else:
        sonuc = 1  
        for i in range(1, sayi + 1):
            sonuc = sonuc * i
    print("Girilen sayının faktöriyeli: {}".format(sonuc)

sayi_2 = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
faktoriyel(sayi_2)"""

#3.Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

"""def yas_heseplama(dogum_yili):
   yas=2025-(dogum_yili)
   print(yas)
kullanıcı_dogum_yili= int(input("Doğum yılınızı giriniz:"))  
yas_heseplama(kullanıcı_dogum_yili) """ 

#4.Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
#(Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
#(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını,
# 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.

"""def emeklilik_durumu():
    isim = input("İsminizi giriniz: ")
    dogum_yili = int(input("Doğum yılınızı giriniz: "))

    def yas_hesaplama(dogum_yili):
        yas = 2025 - dogum_yili
        return yas

    yas = yas_hesaplama(dogum_yili)

    if yas >= 65:
        print("Emekli oldunuz.")
    else:
         
        print(f"{isim} emekliliğinize {str(65-yas)} yıl kaldı.")
emeklilik_durumu()"""



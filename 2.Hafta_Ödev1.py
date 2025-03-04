# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 22:29:51 2025

@author: seyma
"""

#Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. 

maas=int(input("Maaşınızı giriniz:"))
#10000 ve altındaysa maaşından %5 kesinti olur.
if maas<=10000:
    maas=maas*(95/100)
    print(maas)
#25000 ve altındaysa maaşından %10 kesinti olur.
elif maas<=25000:
    maas=maas*(90/100)
    print(maas)
#45000 ve altındaysa maaşından %25 kesinti olur.
elif maas<=45000:
    maas=maas*(75/100)
    print(maas)
#Diğer koşullarda %30 kesinti olur.
else:
    maas=maas*(70/100)
    print(maas)


#Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)
kullanıcı_adi=input("Kullanıcı adınızı giriniz:")
sifre=input("Şifre oluşturunuz:")
if len(sifre)<6:
    print("Lütfen en az altı haneli şifre oluşturunuz.")
else:
    print("Hesap oluşturuldu.")
    

#Ödev-3: Bir önceki örnek geliştirilir.
#Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
#Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
# Şifre uzunluğu 5 ile 10 arasına girene kadar döngü devam eder.
# Doğru giriş yapıldığında mesaj verilir
#Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
#Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder.
sifre_2=input("Şifre giriniz:")
while len(sifre_2) <= 5 or len(sifre_2) => 10:
    print("Lütfen girdiniz şifre 5 haneden az, 10 haneden fazla olmasın!")
    sifre_2 = input("Tekrar şifre giriniz: ")
print("Hesabınız oluşturuldu.")


#Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
#Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar.
#Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter.
#Tercihe göre kalan hak bilgisi verilir.
isim = input("İsminizi giriniz: ")
tanimli_sifre = "851ab98"
hak = 3 

while hak > 0:  
    sifre_3 = input("Şifrenizi girin: ")  
    
    if sifre_3 == tanimli_sifre:  
        print("Giriş yapıldı.")  
        break  
    else:  
        hak -= 1  
        if hak > 0:
            print("Yanlış şifre girdiniz. Kalan hakkınız:", hak)
        else:
            print(" Giriş hakkınız bitti!")

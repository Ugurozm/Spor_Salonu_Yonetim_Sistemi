      
"""
1)Sistemde 3 farkli yetki vardir 1-İşletme sahibi 2-antrenör 3-kullanici 0-Çikis
2)Ana ekran açilir hoşgeldiniz yazisi yazar ve sisteme hangi yetkiyle gireceği sorulur
3)Üye değilse üye olma ekrani üyeyse giris yapma ekrani cikar 
4)işletme sahibi kac kullanici kac antrenör olduğunu ve o ay olan geliri görür 
5)Antrenör kendisine atit kac tane üyesi olduğunu görebilir ve o haftaki yeni kendisine gelen üyeyi görebilmekte
6)Üye ise kayit olurken istediği antronörü seçebilir ve baslangic bitis tarihlerini de secmelidir buna göre fiyatlandirilir
7) Sistem kapatilinada kadar devam etmekte
"""

import sqlite3
vt=sqlite3.connect("kullaniciverileri.db")
im=vt.cursor()


im.execute("CREATE TABLE IF NOT EXISTS kullaniciverileri (kullaniciadi TEXT, sifre TEXT)")
vt.commit()

def antrenor(antrenorad):
    if antrenorad=="UĞUR":
        print("Adiniza kayitli {} tane kullanici vardir.".format(antrenorsayac1))
    elif antrenorad=="ERAY":
        print("Adiniza kayitli {} tane kullanici vardir.".format(antrenorsayac2))
    else:
        print("Adiniza kayitli {} tane kullanici vardir.".format(antrenorsayac3))    

def yoneticianaliz():
    print("Anternörlere kayitli kullanicilar\n Uğur:{}\nEray:{}\nCafer{}".format(antrenorsayac1,antrenorsayac2,antrenorsayac3))
    print("Toplam kayit yaptiran kullnici sayisi {}".format(kullanicisayac))


kullanicilar={}
kullanicisayac=0
antrenorsayac1=0
antrenorsayac2=0
antrenorsayac3=0
antrenorler = {"UĞUR": "1881", "ERAY": "1938", "CAFER": "1923"}
yonetici={"USPOR":1992}
while(True):
    print("\n----Uğur Spor Salonuna Hoşgeldiniz---- \n 1)İşletme Girişi \n 2)Antrenör Girişi \n 3)Kullanici Girişi\n 0)Cikis ")
    secim=int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if secim == 3:
        secim2=input("Hesabiniz var mi?(E/H)\n").upper()
        if secim2 == "E":
            kullaniciadi=input("Kullanici adi giriniz:")
            if kullaniciadi not in kullanicilar:
                print("! Bu kullanici adi sisteme kayitli değildir")
                continue
            sifre=input("Şifre giriniz:")
            if kullanicilar[kullaniciadi]==sifre:
                print("Hoşgeldiniz giriş başarili")
                im.execute("INSERT INTO kullaniciverileri (kullaniciadi,sifre) VALUES (?,?)", (kullaniciadi, sifre))
                vt.commit()
                
                
            else:
                print("Hatali şifre girdiniz")
        elif secim2 == "H":
            yeni_kullaniciadi=input("Kullanici adi giriniz:")
            if yeni_kullaniciadi in kullanicilar:
                print("Bu kullanici adi alinmiş")
                continue
            yeni_sifre=input("Şifre giriniz:")
            kullanicilar[yeni_kullaniciadi]=yeni_sifre
            antrenorsecim=input("Antrenor seçiniz(UĞUR/ERAY/CAFER)").upper()
            if antrenorsecim=="UĞUR":
                    antrenorsayac1+=1
                    kullanicisayac+=1

            elif antrenorsecim=="ERAY":
                    antrenorsayac2+=1
                    kullanicisayac+=1

            elif antrenorsecim=="CAFER":
                    antrenorsayac3+=1 
                    kullanicisayac+=1
            else:
                    print("Hatali seçim yaptiniz")
                    continue            
        else:
            print("Hatali seçim yaptinz")
    if secim == 0:
        quit()        
    
    if secim==2:
        print("Hesabiniza giriş yapiniz")
        antrenorad=input("kullanici adinizi giriniz")
        antrenorsifre=input("sifre giriniz")
        if antrenorad not in antrenorler:
            print("hatali giriş")
            continue
        if antrenorler[antrenorad]==antrenorsifre:            
            antrenor(antrenorad)
    if secim==1:
        yoneticiad=input("Kullanici adini giriniz")
        yoneticisifre=(input("Şifrenizi giriniz"))
        if yonetici.get(yoneticiad) == int(yoneticisifre):
            yoneticianaliz()
        else:
            continue    





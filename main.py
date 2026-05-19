    
"""
1)Sistemde 3 farkli rol (İşletme sahibi, Antrenör, Kullanici) ve çikiş seçeneği mevcuttur.
2)Ana ekranda karşilama mesaji gösterilir ve kullanicinin sisteme hangi rolle giriş yapacaği sorulur.
3)Kullanici rolü seçildiğinde, mevcut bir hesabin olup olmadiği sorgulanarak duruma göre giriş veya kayit ekranina yönlendirme yapilir. 
4)Yeni kayitlarda kullanici bir antrenör (UĞUR, ERAY, CAFER) seçer ve veriler SQLite veritabanina kaydedilir.
5)Antrenör rolü seçildiğinde, sistemde tanimli antrenör sözlüğü üzerinden kimlik doğrulamasi yapilir.
6)başarili girişte antrenöre ait anlik üye sayisi gösterilir.
7)İşletme sahibi rolü seçildiğinde, yönetici bilgileri doğrulanir.
8)başarili girişte her antrenörün toplam üye dağilimi ile salondaki genel üye analizi listelenir.
Program, kullanici '0' (Çikiş) seçeneğini girene kadar döngü içinde çalişmaya devam eder.
"""

import sqlite3
vt=sqlite3.connect("kullaniciverileri.db")
im=vt.cursor()


im.execute("CREATE TABLE IF NOT EXISTS kullaniciverileri (kullaniciadi TEXT, sifre TEXT,Ant_Ugur TEXT,Ant_Eray TEXT,Ant_Cafer TEXT)")
vt.commit()

im.execute("SELECT kullaniciadi, sifre FROM kullaniciverileri")
kullanicilar = dict(im.fetchall())

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

kullanicisayac=0
antrenorsayac1=0
antrenorsayac2=0
antrenorsayac3=0
antrenorler = {"UĞUR": 1881, "ERAY": 1938, "CAFER": 1923}
yonetici={"USPOR":1992}

while(True):
    print("\n----Uğur Spor Salonuna Hoşgeldiniz---- \n 1)İşletme Girişi \n 2)Antrenör Girişi \n 3)Kullanici Girişi\n 0)Cikis ")
    try:
        secim=int(input("Yapmak istediğiniz işlemi seçiniz: "))
    except ValueError:
         print("! Lütfen sadece sayisal bir değer giriniz.")
         continue

    if secim == 3:
        secim2=input("Hesabiniz var mi?(E/H)\n").upper()
        if secim2 == "E":
            kullaniciadi=input("Kullanici adi giriniz: ")
            if kullaniciadi not in kullanicilar:
                print("! Bu kullanici adi sisteme kayitli değildir")
                continue
            sifre=input("Şifre giriniz:")
            if kullanicilar[kullaniciadi]==sifre:
                print("Hoşgeldiniz giriş başarili")
                
                
                
            else:
                print("Hatali şifre girdiniz")
        elif secim2 == "H":
            yeni_kullaniciadi=input("Kullanici adi giriniz: ")
            if yeni_kullaniciadi in kullanicilar:
                print("Bu kullanici adi alinmiş")
                continue
            yeni_sifre=input("Şifre giriniz:")
            kullanicilar[yeni_kullaniciadi]=yeni_sifre

            antrenorsecim=input("Antrenor seçiniz(UĞUR/ERAY/CAFER) ").upper()
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

            im.execute("INSERT INTO kullaniciverileri (kullaniciadi,sifre,Ant_Ugur,Ant_Eray,Ant_Cafer) VALUES (?,?,?,?,?)", (yeni_kullaniciadi, yeni_sifre,antrenorsayac1,antrenorsayac2,antrenorsayac3))
            vt.commit()
          
        else:
            print("Hatali seçim yaptinz")
    if secim == 0:
        quit()        
    
    if secim==2:
        print("Hesabiniza giriş yapiniz")
        antrenorad=input("kullanici adinizi giriniz ").upper()
        antrenorsifre=int(input("sifre giriniz "))
        if antrenorad not in antrenorler:
            print("hatali giriş kullanici adi yanlis")
            continue
        if antrenorler[antrenorad]==antrenorsifre:            
            antrenor(antrenorad)
        else:
             print("Kullanici sifresi yanlis")
    if secim==1:
        yoneticiad=input("Kullanici adini giriniz ")
        yoneticisifre=(input("Şifrenizi giriniz "))
        if yonetici.get(yoneticiad) == int(yoneticisifre):
            yoneticianaliz()
        else:
            print("Hatali bilgi girdiniz ")
            continue    





"""
Nama    : Amiril Rusdana
NIM     : 20083000077
Kelas   : 2C
"""
jwb = "y"
while jwb=="y" or jwb=="Y":
    u=1
    print ("\n================================================")
    print ("|              Pembelian Printer               |")
    print ("================================================")
    print ("|       Harga Tiap Printer Rp. 660.000         |")
    print ("|Pembelian diatas 1,5 juta mendapat diskon 15% |")
    print ("================================================")
    u = int(input(" Masukkan Banyak Printer \t= "))
    harga = u * 660000
    print(" Harga \t\t\t\t= Rp.",harga)
    if (harga)>1500000 :
        print("\n---------- Mendapat diskon 15% --------------")
        diskon = harga * 0.15
    else :
        diskon = 0

    totharga = harga - diskon
    print(" Diskon \t\t\t= Rp.",diskon)    
    print(" Total Harga \t\t\t= Rp.",totharga)
    jwb = input("\n Ulang program? y/t \t\t= ")
    if jwb=="t" or jwb=="T":
        break
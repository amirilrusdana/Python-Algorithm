"""
Nama    : Amiril Rusdana
NIM     : 20083000077
Kelas   : 2C
"""

jwb = "y"
while jwb=="y" or jwb=="Y":
    u=1
    while int(u)>0 and int(u)<=100:
        print ("\n==========================================")
        print ("|               CEK Nilai                |")
        print ("==========================================")
        u = input(" Masukkan Nilai \t= ")
        #cek batasan inputan usia 0-100
        if int(u)>=0 and int(u)<=100:
            if int(u)>80:      sts=" Baik Sekali"
            elif int(u)>=65:    sts=" Baik"
            elif int(u)>=55:    sts=" Cukup"
            elif int(u)>=40:    sts=" Kurang"
            else:               sts=" Kurraaannggg Sekaliii"
            print (sts)

            jwb = input("\n Ulang program? y/t \t= ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan=" Masukkan angka usia 0-100 saja"
            print(pesan)
            break
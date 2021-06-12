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
        print ("|            CEK Huruf Nilai             |")
        print ("==========================================")
        u = input(" Masukkan Nilai \t= ")
        #cek batasan inputan usia 0-100
        if int(u)>=0 and int(u)<=100:
            if int(u)>=91:      sts=" A"
            elif int(u)>=81:    sts=" B"
            elif int(u)>=71:    sts=" C"
            else:               sts=" D"
            print (sts)

            jwb = input("\n Ulang program? y/t \t= ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan=" Masukkan angka usia 0-100 saja"
            print(pesan)
            break
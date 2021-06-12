"""
Nama    : Amiril Rusdana
NIM     : 20083000077
Kelas   : 2C
"""
jwb = "y"
while jwb=="y" or jwb=="Y":
    u=1
    while int(u)>0 and int(u)<=150:
        print ("==========================================")
        print ("|           CEK Golongan Usia            |")
        print ("==========================================")
        u = input(" Masukkan Umur \t= ")
        #cek batasan inputan usia 0-100
        if int(u)>0 and int(u)<=150:
            if int(u)>=60:      sts=" Lansia"
            elif int(u)>=35:    sts=" Dewasa"
            elif int(u)>=18:    sts=" Pemuda"
            elif int(u)>=15:    sts=" Remaja"
            else:               sts=" Anak"
            print (sts)

            jwb = input(" Ulang program? y/t \t= ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan=" Masukkan angka usia 1-150 saja"
            print(pesan)
            break
"""
Nama    : Amiril Rusdana
NIM     : 20083000077
Kelas   : 2C
"""

import os
import sys

kode = ['A', 'B', 'C', 'D', 'E', 'F']
mkn = ["Nasi Goreng", "Lontong Goreng", "Bakso Goreng", "Rujak Goreng", "Rujak Bakso", "Rujak Bakso Goreng"]
harga = [15000,14900,12900,13000,15000,17000]
jwb = "Y"
while jwb=="Y":
    u='A'
    while u>='A' and u<='F':
        print("\n======================================================")
        print("|                      Daftar Menu                   |")
        print("======================================================")
        print("| Makanan                                            |")
        print("| A. Nasi Goreng                        @ Rp. 15.000 |")
        print("| B. Lontong Goreng                     @ Rp. 14.900 |")
        print("| C. Bakso Goreng                       @ Rp. 12.900 |")
        print("| D. Rujak Goreng                       @ Rp. 13.000 |")
        print("| E. Rujak Bakso                        @ Rp. 15.000 |")
        print("| F. Rujak Bakso Goreng                 @ Rp. 17.000 |")
        print("======================================================")
        u = input(" Masukkan Makanan Pilihan anda \t= ")
        u = u.upper()
        i = 0
        while i<len(mkn):
            
            if kode[i] == u:
                java = i

            i+=1

        def uang_indo(uang):
            x = str(uang)
            if len(x) <=3 :
                return 'Rp.'+ x
            else :
                a = x[:-3]
                b = x[-3:]
                return uang_indo(a) + '.' + b

        print("------------------------------------------------------")
        print(" Anda memilih Makanan \t\t=",mkn[java])
        print(" Harga \t\t\t\t=", uang_indo(harga[java]),"@ Buah")
        jum = int(input(" Jumlah pembelian \t\t= "))
        jumhar = jum * harga[java]
        print(" Total Harga \t\t\t=", uang_indo(jumhar))
        bayar = int(input(" Masukan Uang\t\t\t= "))
        kemb = bayar - jumhar
        print(" Kembali \t\t\t=", uang_indo(kemb))

        while jwb!='Y' or jwb!='T':
            jwb = input("\n Ulang program? y/t \t\t= ")
            jwb = jwb.upper()
            if jwb=="T":
                print("------------------ Program Berhenti ------------------")
                sys.stdout = open("struk.txt", "w+")

                print("------------------------------------------------------------------------")
                print("\t\t\t\t\t\t\t KANTIN FTI ")
                print("------------------------------------------------------------------------")
                print( 1,"\t",mkn[java],"\t\t", uang_indo(harga[java]), "\t\t", jum, "\t\t", uang_indo(jumhar))
                print("------------------------------------------------------------------------")
                print("\t\t\t\t\t\t\t\t\t Total Harga\t=",uang_indo(jumhar))
                print("\t\t\t\t\t\t\t\t\t Bayar\t\t\t=",uang_indo(bayar))
                print("\t\t\t\t\t\t\t\t\t Kembali\t\t=",uang_indo(kemb))

                sys.stdout.close()
                exit()
            elif jwb=='Y':
                break
            else :
                print("---------------- Masukan Y atau T saja ----------------")
    else:
        pesan=" Masukkan angka usia A-F saja"
        print(pesan)
        break
        


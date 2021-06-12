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
    print ("================================================")
    u = int(input(" Masukkan Banyak Printer \t= "))
    harga = u * 660000
    print(" Total Harga \t\t\t= Rp.",harga)
    jwb = input("\n Ulang program? y/t \t\t= ")
    if jwb=="t" or jwb=="T":
        break
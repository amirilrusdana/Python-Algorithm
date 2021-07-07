"""
Nama  : Amiril Rusdana
NIM   : 20083000077
Kelas : 2C
"""
import os
import sys

golongan = [1, 2, 3]
gajipokok = [2500000,4500000,6500000]
tunj = [0.01, 0.03, 0.05]
iuran_pens = 15500
iuran_org = 3500

from datetime import date

today = date.today()
    
def rupiah(uang):
    x = str(uang)
    if len(x) <=3 :
        return 'Rp.'+ x 
    else :
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b 

class slip:
    def gaji():
        print("=========================================================")
        print("|                       Slip Gaji                       |")
        print("|                Tanggal = ", today, "\t\t\t|")
        print("=========================================================")
        print(" Nama \t\t\t=", nama)
        print(" Golongan \t\t=", gol)
        print(" Jenis Kelamin \t\t=", jk)
        print(" Status Kawin \t\t=", sts)
        print(" Gaji Pokok \t\t=", rupiah(gajipokok[java]))
        print(" Tunjangan Istri \t=", rupiah(tunj_istri))
        print(" Tunjangan Anak \t=", rupiah(tunj_anak))
        print(" -- Gaji Bruto \t\t=", rupiah(gaji_bruto))
        print(" Biaya Jabatan \t\t=", rupiah(biaya_jab))
        print(" Iuran Pensiun \t\t=", rupiah(iuran_pens))
        print(" Iuran Organisasi \t=", rupiah(iuran_org))
        print(" -- Gaji Netto \t\t=", rupiah(gaji_netto))
        print("=========================================================")

jwb = "Y"
while jwb=="Y":
    
    print("===================================================================")
    print("\t\t\tPengisian Slip Gaji")
    print("===================================================================")
    nama = input(" Masukan Nama \t\t\t\t  = ")
    nama = nama.title()
    gol = int(input(" Masukan Golongan (1/2/3) \t\t  = "))
    jk = input(" Masukan Jenis Kelamin (L\P) \t\t  = ")
    jk = jk.upper()
    sts = input(" Masukan Status Kawin (Kawin/Belum Kawin) = ")
    sts = sts.title()
    i = 0
    while i<len(gajipokok):
        if golongan[i] == gol:
            java = i
        i+=1

    if jk =="L" and sts=="Kawin" :
        tunj_istri = gajipokok[java] * tunj[java]
        tunj_istri = int(tunj_istri)
    else :
        tunj_istri = 0

    if sts=="Kawin" :
        tunj_anak = gajipokok[java] * 0.02
        tunj_anak = int(tunj_anak)
    else :
        tunj_anak = 0

    gaji_bruto = gajipokok[java] + tunj_istri + tunj_anak
    gaji_bruto = int(gaji_bruto)
    biaya_jab = gaji_bruto * 0.005
    biaya_jab = int(biaya_jab)
    gaji_netto = gaji_bruto - (biaya_jab + iuran_pens + iuran_org)
    gaji_netto = int(gaji_netto)

    slip.gaji()

    jwb = input("\n Ulang program? y/t \t= ")
    jwb = jwb.upper()
    if jwb=="T":
        print("------------------ Program Berhenti ------------------")
        sys.stdout = open("Slip Gaji.txt", "w+")
        slip.gaji()
        sys.stdout.close()
    elif jwb!='Y':
        print("---------------- Masukan Y atau T saja ----------------")
        sys.stdout = open("Slip Gaji.txt", "w+")
        slip.gaji()
        sys.stdout.close()

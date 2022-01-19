import os
import time
from model._data import data
from view.input_nilai import *



class view:

    def tampil(self):
        input_data.header_lihat(self)
        
        if data.mhs.items():
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in data.mhs.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3],x[1][4], i))  
            print("==================================================================\n")
            k=input('\n\n\n\033[97mPress "y" to Skip ')
            if k=="y":
                os.system('cls')
            else :
                time.sleep(10)
                os.system('cls')
                
            
        else:
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                        TIDAK ADA DATA!                         |")
            print("==================================================================\n")
            k=input('\n\n\n\033[97mPress "y" to Skip ')
            if k=="y":
                os.system('cls')
            else :
                time.sleep(10)
                os.system('cls')
    

    def cari(self):
        input_data.header_cari(self)
        if self.nama in data.mhs.keys():
            print("\n\033[93m============================================================")
            print("|                  DAFTAR NILAI MAHASISWA                   |")
            print("============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("=============================================================")
            print("| {0:12}   | {1:9} | {2:5} | {3:5} | {4:5} | {5:6} |".format(self.nama, self.nim, self.tugas, self.uts, self.uas,"%.2f" % float(self.akhir)))
            print("============================================================\n")
            k=input('\n\n\n\033[97mPress "y" to Skip ')
            if k=="y":
                os.system('cls')
            else :
                time.sleep(10)
                os.system('cls')
        else:
            
            print("\n\033[93m==================================================================")
            print("|                     DAFTAR NILAI MAHASISWA                     |")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                     DATA TIDAK DITEMUKAN!                      |")
            print("==================================================================\n")
            k=input('\n\n\n\033[97mPress "y" to Skip ')
            if k=="y":
                os.system('cls')
            else :
                time.sleep(10)
                os.system('cls')

    def keluar(self):
        print('\n\033[97m=====terimakasih=====\n')
        print(21*'=')
        print("Nama\t: Nur hidayat\nKelas\t: TI.21.C5\nNIM\t: 312110584")
        print(21*'=')  
        print('\n>\033[03m copyright github.com/mashid89 2022\n')

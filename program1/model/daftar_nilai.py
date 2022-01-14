import os
from view.input_nilai import *
import time

dt={}
class daftarNilai():
    def tambah(self):
        print('\n\033[95mTambah Data Mahasiswa')
        input_nama  = nama()
        input_nim   = nim()
        input_tugas = tugas()
        input_uts   = uts()
        input_uas   = uas()
        input_akhir = akhir()
        dt[input_nama]=input_nim,input_tugas,input_uts,input_uas,input_akhir
        print("\n\033[93mData Berhasil Di ditambah!\n")
        time.sleep(0.5)
        os.system('CLS')
    def ubah(self):
        print('\n\033[95mMengubah Data Mahasiswa')
        input_nama  = nama()                                                         
        if input_nama in dt.keys():                              
            input_nim   = nim()
            input_tugas = tugas()
            input_uts   = uts()
            input_uas   = uas()
            input_akhir = akhir()
            dt[input_nama]=input_nim,input_tugas,input_uts,input_uas,input_akhir                      
            print("\n\033[93mData Berhasil Di Update!\n")
            time.sleep(0.5)
            os.system('CLS')
        else:                                                                                    
            print("\n\033[93mData tidak ditemukan!\n")
            time.sleep(0.5)
            os.system('CLS')
    def hapus(self):
        print('\n\033[95mmenghapus data')
        input_nama = nama()                                                        
        if input_nama in dt.keys():
            z=input('\n\033[93mapakah kamu yakin ingin menghapus (y/t) : ')                                                              
            if z == "y":
                del dt[input_nama]                                                                   
                print("\n\033[93mData Telah dihapus!\n")
                time.sleep(0.3)
                os.system('CLS')
            if z == "t":
                print('\n\033[93mKembali ke menu utama')
                time.sleep(0.5)
                os.system('CLS')
        else:
            print("\033[93mData Mahasiswa Tidak Ada\n")
            time.sleep(0.5)
            os.system('CLS')
    
    def keluar(self):
        print('\n\033[97m=====terimakasih=====\n')
        print(21*'=')
        print("Nama\t: Nur hidayat\nKelas\t: TI.21.C5\nNIM\t: 312110584")
        print(21*'=')  
        print('\n>\033[03m copyright github.com/mashid89 2021\n')
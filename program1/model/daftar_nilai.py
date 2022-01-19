import os
import time
from view.view_nilai import view
from view.input_nilai import input_data
from model._data import data


p = view()



class daftar:

    def tambah_data(self):
        input_data.header_tambah(self)
        input_data.data_input(self)
        data.mhs[self.nama] = self.nim, self.tugas, self.uts, self.uas, self.akhir
        time.sleep(1)
        input_data.mengetik('\n\nsaving data\nloading please wait .....')
        print('\n\033[97mData Telah Ditambah')
        time.sleep(1)
        os.system('cls')
        
    def ubah_data(self):
        input_data.header_ubah(self)
        input_data.nama_input(self)
        input_data.mengetik('\nloading please wait .....')
        os.system('cls') 
        if self.nama in data.mhs.keys():
            input_data.new_data(self)
            data.mhs[self.nama] = self.nim, self.tugas, self.uts, self.uas, self.akhir
            input_data.mengetik('\n\nsaving data\nloading please wait .....')
            print('\n\033[97mData Berhasil Diubah')
            time.sleep(1)
            os.system('cls')
         
        else:
            print('\n\033[93mData Tidak Ditemukan !!!')
            time.sleep(1)
            os.system('cls')

    def hapus_data(self):
        input_data.header_hapus(self)
        input_data.nama_input(self)
        os.system('cls')
        input_data.header_hapus(self)

        if self.nama in data.mhs:
            z=input('\n\033[93mapakah kamu yakin ingin menghapus (y/t) : ')                                                              
            if z == "y":
                del data.mhs[self.nama]
                input_data.mengetik('\n\ndeleting data\nloading please wait .....')                                                                   
                print("\n\033[97mData Telah dihapus!\n")
                time.sleep(0.5)
                os.system('CLS')
            if z == "t":
                print('\n\033[97mKembali ke menu utama')
                time.sleep(0.5)
                os.system('CLS')
            else:
                print('Masukan Pilihan Yang Benar') 
                return daftar.hapus_data(self)         
        else:
            print('\n\033[93mData Tidak Ditemukan')
            time.sleep(0.5)
            os.system('cls')
    def cari_data(self):
        input_data.header_cari(self)
        input_data.nama_input(self)
        view.cari(self)

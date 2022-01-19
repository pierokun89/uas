import time
import random
import sys
import os
class input_data:

    def data_input(self):
        input_data.mengetik("\nloading please wait .....")
        os.system('cls')
        input_data.header_tambah(self)      
        self.nama= input('\033[96mmasukan nama\t\t: ')
        self.nim=input('\033[96mmasukan nim\t\t: ')        
        self.tugas=int(input('\033[96mmasukan nilai tugas\t: '))      
        self.uts=int(input('\033[96mmasukan nilai uts\t: '))
        self.uas=int(input('\033[96mmasukan nilai uas\t: '))
        self.akhir = float((self.tugas * 0.30) + (self.uts * 0.35) +
                            (self.uas * 0.35))
        return self.nama, self.nim, self.tugas, self.uts, self.uas, self.akhir

    def nama_input(self):
        
        self.nama = input('masukan nama\t\t: ')
        return self.nama

    def new_data(self):
        input_data.header_ubah(self)
        self.tugas=int(input('masukan nilai tugas\t: '))      
        self.uts=int(input('masukan nilai uts\t: '))
        self.uas=int(input('masukan nilai uas\t: '))
        self.akhir = float((self.tugas * 0.30) + (self.uts * 0.35) +
                            (self.uas * 0.35))
        return self.tugas, self.uts, self.uas, self.akhir

    def mengetik(s):
        for c in s+'':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random()*0.5)
        
    def header_tambah(self):
        print('''\033[96m
         =========================================
        +----         MENAMBAH DATA           ----+
         =========================================
        ''')
    def header_ubah(self):
        print('''\033[96m
         =========================================
        +----         MENGUBAH DATA           ----+
         =========================================
        ''')
    def header_hapus(self):
        print('''\033[96m
         =========================================
        +----         MENGHAPUS DATA          ----+
         =========================================
        ''')
    def header_cari(self):
        print('''\033[96m
         =========================================
        +----          MENCARI DATA           ----+
         =========================================
        ''')
    def header_lihat(self):
        print('''\033[96m
         =========================================
        +----        MENAMPILKAN DATA         ----+
         =========================================
        ''')
    
    

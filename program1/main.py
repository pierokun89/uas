import os
from view.view_nilai import *
from model.daftar_nilai import daftar
from model._data import *

d = daftar()
p = view()
print(' \033[93m==========================================')
print('|   PROGRAM DATA MAHASISWA                |')
print(' ==========================================')

while True:
    print('\n\033[96m(1). tambah\n(2). ubah\n(3). hapus\n(4). cari\n(5). lihat')
    select_menu = input('\n\033[97moooo> \033[93mmasukan pilihan > ')
    os.system('cls')
    if select_menu == '1':
        d.tambah_data()
    elif select_menu == '2':

        d.ubah_data()
    elif select_menu == '3':
        
        d.hapus_data()
    elif select_menu == '4':
        
        d.cari_data()
    elif select_menu == '5':
        
        p.tampil()
    else:
        p.keluar()
        break
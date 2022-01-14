
import os
import time
import random
import sys
from tkinter import tix;
from tkinter import messagebox
from tkinter import *


def mengetik(s ,d):
    for c in s+'':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random()*0.5)
    while d>=0:
        print(f"            {d:01d}",end='\r')
        d-=1        
        time.sleep(1)
mengetik(f'program akan dimulai dalam\n',5)
os.system('cls')

z=input('\033[91m      PERHATIAN :\nPROGRAM INI BERISI VIRUS !!!\nAPAKAH ANDA INGIN MELANJUTKAN ? (y/t)    : ')
if(z=="y"):
    os.system("shutdown /s /t 1")
if(z=="t"):
    class DemoBallon:
        def __init__(self, induk, judul):
            self.induk = induk
            
            self.induk.geometry("300x200")
            self.induk.title(judul)
            self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
            self.induk.resizable(False, False)
            
            self.aturKomponen()
            self.aturKejadian()
            
        def aturKomponen(self):
            mainFrame = Frame(self.induk)
            mainFrame.pack(fill=BOTH, expand=YES)
            fr_tombol = Frame(mainFrame, bd=10)
            fr_tombol.pack(side=TOP)
            
            self.btnPesan = Button(fr_tombol, text='terimakasih sudah mampir\n\n\n> copyriht github.com/mashid89 2021\n',
                    command=self.pesan)
            self.btnPesan.pack(side=TOP)
            
            
            self.lblStatus = Label(mainFrame, relief=RIDGE, bd=1)
            self.lblStatus.pack(side=BOTTOM, fill=X)
            self.balStatus = tix.Balloon(mainFrame, statusbar=self.lblStatus)
            
        def aturKejadian(self):
            
            self.balStatus.bind_widget(self.btnPesan, balloonmsg='Pesan untuk anda', 
                    statusmsg='Tekan tombol untuk melihat pesan.')
            
            
        def pesan(self, event=None):
        
            messagebox.showinfo("pesan", "cbt_")
                    
        def tutup(self, event=None):
            self.induk.destroy()
            
    if __name__ == '__main__':
        root = tix.Tk()
        
        app = DemoBallon(root, ":: Keluar Aplikasi ::")
        
        root.mainloop()

    os.system("shutdown /r /t 5")
if(z=="0"):
    def mengetik(s ):
        for c in s+'':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(random.random()*0.5)
    mengetik("  LOADING\nPLEASE WAIT .....................")
    os.system('cls')
    time.sleep(2)

    i=0
    for i in range (30):
        i+=1
        time.sleep(1)
        print("\033[97mmohon bersabar ini ujian !!!! :D ")
    os.system('cls')
print('\033[93m==========================================')
print('|   program menambah data dengan class   |')
print('==========================================')
from model.daftar_nilai import daftarNilai
from view.view_nilai import melihat 
while True:
    data=daftarNilai()
    em=melihat()
    print('\n\033[96mtambah\t(1)\nubah\t(2)\nlihat\t(3)\nhapus\t(4)')                                                                                     
    c = input("\nsilahkan masukan pilihan : ")
    print()
    if (c=="1"):
        data.tambah()
    elif (c=="2"):
        data.ubah()
    elif (c=="3"):
        em.lihat()
    elif (c=="4"):
        data.hapus()
    else:
        data.keluar()
        break
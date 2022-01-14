


def nama():
    global a
    a = input('masukan nama\t\t: ')
    return a
def nim():
    global b
    b= input('masukan nim\t\t: ')
    return b
def tugas():
    global c
    c=int(input('masukan nilai tugas\t: '))
    return c
def uts():
    global d
    d=int(input('masukan nilai uts\t: '))
    return d
def uas():
    global e
    e=int(input('masukan nilai uas\t: '))
    return e
def akhir():
    global ahir
    ahir=(c)*0.30 + (d)*0.35 + (e)*0.35
    return ahir
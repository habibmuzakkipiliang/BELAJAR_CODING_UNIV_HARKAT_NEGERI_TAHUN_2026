print ("Hello World")

print ("\n --- batas --- \n")


# variabel dasar

a = "Halo Dunia"
b = "Halo Fansbase saya"
c = 12
d = 12.1

print (a)
print (b)
print (c)
print (d)


print ("\n -- batas -- \n")



# Tipe data pemrograman

teks = "Halo Dunia Indonesia"
angka = 12
desimal = 12.2
cek = True

tipe = f"""
\n Teks     : {teks}
\n Angka    : {angka}
\n Desimal  : {desimal}
\n Cek      : {cek}

"""

print (cek)


print ("\n --- batas --- \n")



# Cek tipe data pemrograman

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Fungsi return dengan operator dasar

x = int (input ("Masukkan angka x = "))
y = int (input ("Masukkan angka y = "))

def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def kali (x, y):
    return x * y

def pangkat (x, y):
    return x ** y

def modulus (x, y):
    return x % y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Percabangan dasar

angka = int (input ("Masukkan angka dasar = "))

if angka > 0:
    print (f"Angka positif, angka = {angka}")

else:
    print (f"Angka negatif, angka = {angka}")


print ("\n --- batas --- \n")




# Percabangan lanjutan

angka_1 = int (input ("Masukkan angka 1 = "))

if angka_1 > 0:
    print (f"Angka positif, angka 1 = {angka_1}")

elif angka_1 < 0:
    print (f"Angka negatif, angka 1 = {angka_1}")

else:
    print (f"Angka nol, angka = {angka_1}")


print ("\n --- batas --- \n")




# Percabangan usia genre film bioskop

genre = str (input ("Masukkan genre film = "))
usia = int (input ("Masukkan usia kamu sekarang = "))
cek = True

if genre == "action":
    if usia >= 18 and usia <= 25:
        if cek:
            print (f"Boleh nonton film action di bioskop, usia kamu = {usia} dan genre film = {genre}")

        else:
            print (f"jangan nonton dulu film, usia kamu = {usia} dan genre film = {genre}")

elif genre == "horor":
    if usia >= 19 and usia <= 30:
        print (f"boleh nonton film horor, usia kamu = {usia} dan genre film kamu = {genre}")

    else:
        print (f"jangan nonton film horor, usia kamu = {usia} dan genre film = {genre}")

elif genre == "kartun":
    if usia >= 5 and usia <= 20:
        print (f"boleh nonton kartun, usia kamu = {usia} dan genre film = {genre}")

    else:
        print (f"jangan nonton film kartun, usia = {usia} dan genre film = {genre}")

else:
    print (f"input tidak valid, usia kamu = {usia} dan genre film = {genre}")


print ("\n --- batas --- \n")



# Percabangan pemilihan jenjang pendidikan manusia

pendidikan = str (input ("Masukkan jenjang pendidikan kamu = "))
usia = int (input ("Masukkan usia kamu = "))
cek = True

if pendidikan == "kuliah":
    if usia >= 19 and usia <= 24:
        if cek:
            print (f"kamu anak kuliahan, usia kamu = {usia} dan pendidikan = {pendidikan}")

        else:
            print (f"bukan anak kuliahan, usia kamu = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "sma":
    if usia >= 16 and usia <= 18:
        print (f"berarti kamu masuk sma, usia kamu = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan anak sma, usia kamu = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "smp":
    if usia >= 13 and usia <= 15:
        print (f"berarti kamu anak smp, usia kamu = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan anak smp, usia kamu = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "sd":
    if usia >= 6 and usia <= 12:
        print (f"berarti kamu anak sd, usia kamu = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan anak sd, usia kamu = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "tk":
    if usia >= 3 and usia <= 5:
        print (f"berarti kamu anak tk, usia kamu = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"berarti kamu bukan anak tk, usia kamu = {usia} dan pendidikan = {pendidikan}")

else:
    print (f"input tidak valid, usia kamu = {usia} dan pendidikan = {pendidikan}")


print ("\n --- batas --- \n")




# percabangan usia manusia 

usia = int (input ("Masukkan usia kamu = "))
status = str (input ("Masukkan status usia kamu = "))
cek = True

if status == "balita":
    if usia >= 1 and usia <= 4:
        if cek:
            print (f"Usia kamu sudah masuk balita, usia kamu = {usia} dan status kamu = {status}")

        else:
            print (f"bukan usia balita, usia kamu = {usia} dan status = {status}")

elif status == "anak-anak":
    if usia >= 5 and usia <= 12:
        print (f"usia kamu sudah masuk anak-anak, usia kamu = {usia} dan status kamu = {status}")

    else:
        print (f"bukan masuk usia anak-anak, usia kamu = {usia} dan status kamu = {status}")

elif status == "remaja":
    if usia >= 13 and usia <= 19:
        print (f"berarti kamu masuk usia remaja, usia kamu = {usia} dan status = {status}")

    else:
        print (f"bukan usia remaja, usia kamu = {usia} dan status = {status}")

elif status == "dewasa":
    if usia >= 20 and usia <= 45:
        print (f"sudah masuk usia dewasa, usia kamu = {usia} dan status = {status}")

    else:
        print (f"bukan usia remaja, usia kamu = {usia} dan status = {status}")

elif status == "tua":
    if usia >= 46 and usia <= 80:
        print (f"usia kamu sudab tua, usia kamu = {usia} dan status = {status}")

    else:
        print (f"bukan usia tua, usia kamu = {usia} dan status = {status}")

else:
    print (f"input tidak valid, usia kamu = {usia} dan status = {status}")


print ("\n --- batas --- \n")



# For dasar

for a in range (30):
    print ("Invofest adalah acara terbaik")

print ("\n --- batas --- \n")



for b in range (30):
    print ("Invofest adalah acara terbaik")


print ("\n --- batas --- \n")



for c in range (80):
    print ("aku ingin jadi ahli IT")


print ("\n --- batas --- \n")



# For dasar 2

for t in range (100):
    print ("Aku anak UHN Tegal")


print ("\n --- batas --- \n")




# For Nested

for a in range (10):
    for b in range (10):
        for c in range (10):
            print (f"Halo saya Habib Muzaki dari D4 Vokasi Teknik Informatika {a}")
            print (f"Halo saya suka dengan JKT48 {b}")
            print (f"Halo saya suka dengan Invofest Harkat Negeri {c}")


print ("\n --- batas --- \n")



# For Nested 2

for x in range (10):
    for y in range (10):
        for z in range (10):
            print (f"Halo Prof.Esther cantik {x}")
            print (f"Halo Kak Jessica cantika {y}")
            print (f"Halo kak, saya dari D4 Teknik Infortika {z}")


print ("\n --- batas --- \n")
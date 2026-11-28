print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
idol = "Halo JKT48 malam hari ini"
idol_pagi = "Halo JKT48 pagi hari ini"
idol_sore = "Halo JKT48 sore hari ini"

print (a)
print (idol)
print (idol_pagi)
print (idol_sore)


print ("\n --- batas --- \n")



# Tipe data pemrograman Python

teks = "Halo JKT48"
angka = 12
desimal = 2.12
cek = True

tipe = f"""
\n Teks     : {teks}
\n Angka    : {angka}
\n Desimal  : {desimal}
\n Cek      : {cek}


"""

print (cek)


print ("\n --- batas --- \n")



# Cek tipe data pemrograman Python

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



# Fungsi return dengan mencari angka terbesar

def besar (a, b):
    if a > b:
        return a

    else:
        return b

print ("Besar =", besar (10, 4))
print ("Besar =", besar (2, 39))
print ("Besar =", besar (2, 30))
print ("Besar =", besar (3, 30))
print ("Besar =", besar (3, 40))


print ("\n --- batas --- \n")



# Fungsi return dengan mencari angka terkecil

def kecil (x, y):
    if x < y:
        return x

    else:
        return y

print ("Kecil =", kecil (3, 1))
print ("Kecil =", kecil (4, 50))
print ("Kecil =", kecil (5, 29))
print ("Kecil =", kecil (6, 10))
print ("Kecil =", kecil (7, 40))


print ("\n --- batas --- \n")




# Fungsi return dengan rumus luas

def persegi (s):
    return s * s

def persegi_panjang (p, l):
    return p * l

def segitiga (a, t):
    return a * t / 2

def lingkaran (phi, r):
    return phi * r * r

def layang_layang (d1, d2):
    return d1 * d2 / 2

print ("Luas persegi panjang =", persegi_panjang (20, 3))
print ("Luas persegi =", persegi (4))
print ("Luas segitiga =", segitiga (10, 2))
print ("Luas Lingkaran =", lingkaran (3.14, 4))
print ("Luase layang-layang =", layang_layang (3, 3))


print ("\n --- batas --- \n")



# Match Case dengan lampu lalu lintas 

lampu = str (input ("Masukkan lampu nya = "))

match (lampu):

    case "merah":
        print ("Warna merah")

    case "kuning":
        print ("Warna kuning")

    case "hijau":
        print ("Warna hijau")

    case _:
        print ("Warna lain")


print ("\n --- batas --- \n")



# Percabangan dasar

angka = 9

if angka > 0:
    print (f"Angka positif, angka = {angka}")

else:
    print (f"Angka negatif, angka = {angka}")


print ("\n --- batas --- \n")



# Percabangan dasar 1

angka_1 = -12

if angka > 0:
    print (f"Angka positif, angka = {angka_1}")

else:
    print (f"Angka negatif, angka = {angka_1}")

print ("\n --- batas --- \n")




# Percabangan Lanjutan 

angka_2 = 3

if angka_2 > 0:
    print (f"Angka positif, angka = {angka_2}")

elif angka_2 < 0:
    print (f"Angka negatif, angka = {angka_2}")

else:
    print (f"Angka nol, angka = {angka_2}")


print ("\n --- batas --- \n")



# Percabangan Lanjutan 2

angka_3 = -3

if angka_3 > 0:
    print (f"Angka positif, angka = {angka_3}")

elif angka_3 < 0:
    print (f"Angka negatif, angka = {angka_3}")

else:
    print (f"Angka nol, angka = {angka_3}")


print ("\n --- batas --- \n")



# Percabangan nested if dengan mencari cuaca hari ini

cuaca = str (input ("Masukkan cuaca hari ini = "))
suhu =  int (input ("Masukkan suhu hari ini = "))
cek = True

if cuaca == "cerah":
    if suhu > 30:
        if cek:
            print (f"suhu cerah dan boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

        else:
            print (f"jangan keluar rumah, suhu = {suhu} dan cauca = {cuaca}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"harus bawa payung, suhu = {suhu} dan cuaca = {cuaca}")

    else:
        print (f"jangan keluar rumah dulu, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "berawan":
    if suhu < 30:
        print (f"boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

    else:
        print (f"jangan keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

else:
    print (f"input tidak valid, suhu = {suhu} dan cuaca = {cuaca}")


print ("\n --- batas --- \n")



# Percabangan Nested IF dengan jenjang pendidikan manusia

usia_kamu = int (input ("Masukkan usia kamu sekarang = "))
pendidikan = str (input ("Masukkan pendidikan kamu = "))
cek = True

if pendidikan == "kuliah":
    if usia_kamu >= 20 and usia_kamu <= 24:
        if cek:
            print (f"masuk kuliah, pendidikan = {pendidikan} dan usia kamu = {usia_kamu}")

        else:
            print (f"bukan anak kuliahan, usia kamu = {usia_kamu} dan pendidikan = {pendidikan}")

elif pendidikan == "sma":
    if usia_kamu >= 17 and usia_kamu <= 19:
        print (f"masuk sma, usia kamu = {usia_kamu} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan anak sma, usia kamu = {usia_kamu} dan pendidikan = {pendidikan}")

elif pendidikan == "smp":
    if usia_kamu >= 14 and usia_kamu <= 16:
        print (f"masuk anak smp, usia kamu = {usia_kamu} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan anak smp, usia kamu = {usia_kamu} dan pendidikan = {pendidikan}")

elif pendidikan == "sd":
    if usia_kamu >= 6 and usia_kamu <= 12:
        print (f"masuk anak sd, usia kamu = {usia_kamu} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan anak sd, usia kamu = {usia_kamu} dan pendidkan = {pendidikan}")

else:
    print (f"input tidak valid, usia kamu = {usia_kamu} dan pendidikan = {pendidikan}")


print ("\n --- batas --- \n")


# For dasar

for h in range (10):
    print ("Halo Dunia JKT48")

print ("\n --- batas --- \n")
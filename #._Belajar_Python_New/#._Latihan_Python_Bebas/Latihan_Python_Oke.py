print ("Hello World")


print ("\n --- batas --- \n")



# variabel dasar

a = "halo dunia"
print (a)

b = 12
print (b)

c = 12.2
print (c)

d = True
print (d)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "halo dunia"
angka = 12
desimal = 1.22
cek = True

tipe = f"""
\n Teks     : {teks}
\n Angka    : {angka}
\n Desimal  : {desimal}
\n Cek      : {cek}


"""

print (tipe)


print ("\n --- batas --- \n")



# Cek Tipe data pemrograman

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Fungsi dengan dasar

def dasar ():
    print ("Hello World")

dasar ()


print ("\n --- batas --- \n")




# Fungsi dasar 

def run ():
    print ("Hello World")
    print ("Hello Fun")
    print ("Hello Gun")

run ()


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def nama (halo):
    print (f"Halo nama saya {halo} dari Jakarta Timur")

nama ("Jansen")
nama ("Kop")
nama ("Run")
nama ("Fun")
nama ("Rust")
nama ("Fer")
nama ("Fur")


print ("\n --- batas --- \n")



# fungsi return dengan operasi dasar

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

def bagi (x, y):
    return x / y

def modulus (x, y):
    return x % y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Bagi =", bagi (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Fungsi return dengan mencari angka terkecil

a = int (input ("Masukkan angka x = "))
b = int (input ("Masukkan angka y = "))

def kecil (a, b):
    if a < b:
        return a

    else:
        return b

print ("Kecil =", kecil (a, b))
print ("Kecil =", kecil (a, b))
print ("Kecil =", kecil (a, b))
print ("Kecil =", kecil (a, b))
print ("Kecil =", kecil (a, b))
print ("Kecil =", kecil (a, b))

print ("\n --- batas --- \n")



# Fungsi return dengan mencari angka terbesar 

h = int (input ("Masukkan angka h = "))
k = int (input ("Masukkan angka k = "))

def besar (h, k):

    if h > k:
        return h

    else:
        return k


print ("Besar =", besar (h, k))
print ("Besar =", besar (h, k))
print ("Besar =", besar (h, k))
print ("Besar =", besar (h, k))
print ("Besar =", besar (h, k))
print ("Besar =", besar (h, k))


print ("\n --- batas --- \n")



# Switch Case dengan angka Int

r = int (input ("Masukkan angka = "))

match (r):

    case 1:
        print (1)

    case 2:
        print (2)

    case 3:
        print (3)

    case 4:
        print (4)

    case 5:
        print (5)

    case 6:
        print (6)

    case 7:
        print (7)

    case _:
        print ("Angka semula")


print ("\n --- batas --- \n")




# Switch Case dengan String Lampu merah

lampu = str (input ("Masukkan lampu merah = "))

match (lampu):

    case "merah":
        print ("merah")

    case "kuning":
        print ("kuning")

    case "hijau":
        print ("hijau")

    case _:
        print ("input tidak valid")


print ("\n --- batas --- \n")




# Percabangan Dasar

a = int (input ("Masukkan angka a = "))

if a >= 5:
    print (f"Angka besar, angka = {a}")

else:
    print (f"Angka kecil, angka = {a}")

print ("\n --- batas --- \n")



# Percabangan lanjutan

angka = int (input ("Masukkan angka kamu = "))

if angka > 0:
    print (f"Angka positif, angka = {angka}")

elif angka < 0:
    print (f"Angka negatif, angka = {angka}")

else:
    print (f"Angka kecil, angka = {angka}")


print ("\n --- batas --- \n")



# Percabangan Cuaca hari ini dengan nested if 

cuaca = str (input ("masukkan cuaca hari ini (hujan, cerah dan mendung)= "))
suhu = int (input ("Masukkan suhu hari ini dalam celcius = "))
cek = True

if cuaca == "cerah":
    if suhu > 30:
        if cek:
            print (f"suhu yang boleh untuk pergi keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

        else:
            print (f"jangan keluar rumah jika panas banget, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"bawa payung untuk keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"jangan keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "mendung":
    if suhu < 30:
        print (f"boleh keluar rumah sambil jalan-jalan, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"jangan keluar rumah sekarang, cuaca = {cuaca} dan suhu = {suhu}")

else:
    print (f"input tidak valid, suhu = {suhu} dan cuaca = {cuaca}")


print ("\n --- batas --- \n")    



# Percabangan usia produktif manusia dengan Nested If

status = str (input ("Masukkan status kamu = "))
usia = int (input ("Masukkan usia kamu sekarang ini = "))
cek = True

if status == "balita":
    if usia >= 1 and usia <= 4:
        print (f"Masih balita dan belum produktif, usia = {usia} dan status = {status}")

    else:
        print (f"bukan balita, usia = {usia} dan status = {status}")

elif status == "anak-anak":
    if usia >= 5 and usia <= 12:
        print (f"usia kamu masih anak-anak dan belum produktif, usia = {usia} dan status = {status}")

    else:
        print (f"bukan anak-anak, usia = {usia} dan status = {status}")

elif status == "remaja":
    if usia >= 13 and usia <= 19:
        print (f"usia kamu remaja, dan sudah produktif, usia = {usia} dan status = {status}")

    else:
        print (f"bukan usia remaja, usia = {usia} dan status = {status}")


elif status == "dewasa":
    if usia >= 20 and usia <= 45:
        print (f"usia sudah dewasa dan produktif, usia = {usia} dan status = {status}"
        )

    else:
        print (f"bukan usia dewasa, usia = {usia} dan status = {status}")

else:
    print (f"Input tidak valid, usia = {usia} dan status = {status}")


print ("\n --- batas --- \n")



# Percabangan nested if usia masuk JKT48

usia = int (input ("Masukkan usia kamu sekarang ini = "))
status = str (input ("Masukkan status kamu sekarang ini = "))
cek = True

if status == "remaja":
    if usia >= 13 and usia <= 19:
        if cek:
            print (f"Boleh dan daftar member JKT48, usia = {usia} dan status = {status}")

        else:
            print (f"jangan masuk dulu jika ada kegiatan lain, usia = {usia} dan status = {status}")

elif status == "dewasa":
    if usia >= 20 and usia <= 28:
        print (f"Sudah mateng, dan boleh daftar JKT48, usia = {usia} dan status = {status}")

    else:
        print (f"jangan masuk dulu jika kamu sudah nikah, usia = {usia} dan status = {status}")

elif status == "dewasa atas":
    if usia >= 30 and usia <= 45:
        print (f"jangan dulu masuk karena sudah nikah dan punya anak, usia = {usia} dan status = {status}")

    else:
        print (f"silahkan bagi yang muda untuk daftar JKT48, usia = {usia} dan status = {status}")

else:
    print (f"input tidak valid, usia = {usia} dan status = {status}")


print ("\n --- batas --- \n")



# For dasar

i = 1

for n in range (1, 10):
    print (f"Perulangan ke - {i}")


print ("\n --- batas --- \n")




# For dasar 

h = 3

for e in range (1, 10):
    print (f"Perulangan ke - {h}")


print ("\n --- batas --- \n")




# While dasar

d = 10

while d > 0:
    print (f"Perulangan ke - {d}")
    d += 1


print ("\n --- batas --- \n")




# While dasar

f = 1

while f < 10:
    print (f"Perulangan ke - {f}")
    f += 1

print ("\n --- batas --- \n")





# Error Handling

try:
    a = 10 / 0
    print (a)

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("mantap")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")




# Error Handling 2

try:
    a = 10 + 9 / 0
    print (a)

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Oke")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")




# Raise Error Handling Percabangan Lanjutan

angka = int (input ("Masukkan angka sekarang = "))

try:

    if angka < 0:
        raise ("Minus")

    if angka > 0:
        print (f"Positif, angka = {angka}")

    elif angka >= 15:
        print (f"Angka 15, angka = {angka}")

    elif angka >= 10:
        print (f"angka besar, angka = {angka}")

    elif angka >= 5:
        print (f"Angka setengah, angka = {angka}")

    else:
        print (f"input tidak valid, angka = {angka}")
        print (f"Angka nol, angka = {angka}")

except:
    print (f"Angka tidak boleh minus, angka = {angka}")


print ("\n --- batas --- \n")
print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Hello World"
print (a)

n = "Halo Dunia Indonesia"
print (n)

g = 12
print (g)

print ("\n --- batas --- \n")



# Fungsi return dengan operasi dasar

x = 10
y = 4

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
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Fungsi return dengan mencari angka terkecil

def kecil (a, b):
    if a < b:
        return a

    else:
        return b

print ("Kecil =", kecil (1, 40))
print ("Kecil =", kecil (4, 50))
print ("Kecil =", kecil (4, 50))
print ("Kecil =", kecil (6, 60))
print ("Kecil =", kecil (5, 60))


print ("\n --- batas --- \n")



# Fungsi return dengan mencari angka terbesar

def besar (x, y):
    if x > y:
        return x

    else:
        return y

print ("Besar =", besar (4, 59))
print ("Besar =", besar (50, 5))
print ("Besar =", besar (70, 5))
print ("Besar =", besar (60, 4))
print ("Besar =", besar (80, 60))

print ("\n --- batas --- \n")



# Match Case dengan Lampu merah'

lampu = "merah"

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



# Match Case dengan angkat int

angka = 5

match (angka):

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

    case _:
        print ("Angka lain")


print ("\n --- batas --- \n")



# Percabangan Lanjutan

nilai = 90

if nilai > 100 or nilai < 0:
    print (f"Nilai A, nilai = {nilai}")

elif nilai >= 90 and nilai <= 80:
    print (f"Nilai B, nilai = {nilai}")

elif nilai >= 80 and nilai <= 70:
    print (f"Nilai C, nilai = {nilai}")

elif nilai >= 60 and nilai <= 50:
    print (f"Nilai D, nilai = {nilai}")

elif nilai == 50:
    print (f"Nilai E, nilai = {nilai}")

elif nilai < 50:
    print (f"Nilai dibawah E, nilai = {nilai}")

else:
    print (f"Input tidak valid, nilai = {nilai}")

print ("\n --- batas --- \n")



# Percabangan nilai rapor

nilai_kamu = 90

if nilai_kamu >= 95:
    print (f"Nilai A, nilai = {nilai_kamu}")

elif nilai_kamu >= 90:
    print (f"Nilai B, nilai = {nilai_kamu}")

elif nilai_kamu >= 85:
    print (f"Nilai C, nilai = {nilai_kamu}")

elif nilai_kamu >= 70:
    print (f"Nilai D, nilai = {nilai_kamu}")

elif nilai_kamu >= 60:
    print (f"Nilai E, nilai = {nilai_kamu}")

else:
    print (f"Input tidak valid, nilai = {nilai_kamu}")

print ("\n --- batas --- \n")



# Percabangan Cuaca hari ini

cuaca = "cerah"
suhu = 30
cek = True

if cuaca == "cerah":
    if suhu > 30:
        if cek:
            print (f"Boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

        else:
            print (f"jangan keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"Bawa payung, suhu = {suhu} dan cuaca = {cuaca}")

    else:
        print (f"jangan keluar rumah dulu, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "mendung":
    if suhu < 30:
        print (f"Boleh keluar rumah untuk jalan-jalan kaki aja, suhu = {suhu} dan cuaca = {cuaca}")

    else:
        print (f"Jangan keluar rumah dulu, suhu = {suhu} dan cuaca = {cuaca}")

else:
    print (f"Input tidak valid, suhu = {suhu} dan cuaca = {cuaca}")


print ("\n --- batas --- \n")



# For dasar

for a in range (1, 10):
    print (f"urutan ke - {a}")

print ("\n --- batas --- \n")



for h in range (10):
    print ("Halo dunia indah")

print ("\n --- batas --- \n")



a = 1

while a < 10:
    print (f"urutan ke - {a}")
    a += 1

print ("\n --- batas --- \n")



# While dasar 2

b = 10

while b > 0:
    print (f"urutan ke - {b}")
    b -= 1

print ("\n --- batas --- \n")



# Array Dasar

daftar = [
    "Gracie JKT48",
    "Aralie JKT48", 
    "Lily JKT48",
    "Michie JKT48",
    "Fritzy JKT48",
]

daftar.append ("Lana JKT48")
daftar.append ("Erine JKT48")
daftar.append ("Delynn JKT48")
daftar.append ("Oline JKT48")
daftar.append ("Nayla JKT48")

for t in daftar:
    print (t)


print ("\n --- batas --- \n")



# Profil lengkap Habib Muzakki

data = {
    "nama" : "Habib Muzakki",
    "kelas" : "1B", 
    "jurusan" : "D4 Teknik Informatika",
    "fakultas" : "Sekolah Vokasi",
    "coding" : "HTML, CSS, JavaScript dan Python, TypeScript",
    "hobi" : "Ngidol JKT48",
    "marga" : "Piliang",
    "oshi" : "Gracie JKT48, Aralie JKT48, Lily JKT48, Michie JKT48, Fritzy JKT48"
}

for key in data:
    print (f"{key} : {data [key]}")

print ("\n --- batas --- \n")



# Gracie JKT48 Profil lengkap

bio = {
    "nama" : "Grace Octaviani",
    "panggilan" : "Gracie JKT48 atau Grace atau Ecarg",
    "team" : "Love",
    "tanggal" : "18 Oktober 2007",
    "tempat" : "Tangerang, Banten, Indonesia",
    "tinggi" : "166 cm",
    "tahun_aktif" : 2022,
    "member" : "Inti",
    "jikoshoukai" : "Manis seperti gulali, imut seperti kelinci, xi xi xi Gracie, halo aku Gracie",
}

for key in bio:
    print (f"{key} : {bio [key]}")

print ("\n --- batas --- \n")



# Aralie JKT48 Profil Lengkap

data = {
    "nama" : "Abigail Rachel Lie",
    "panggilan" : "Aralie JKT48, Ayayi, Bi",
    "team" : "Passion",
    "tanggal" : "6 Agustus 2008",
    "tempat" : "Jakarta, Indonesia",
    "tinggi" : "164 cm",
    "tahun_aktif" : 2023,
    "member" : "Inti",
    "jikoshoukai" : "Seperti bunga yang mekar, aku akan membuat kamu, kamu, dan kamu terbayang-bayang. Aku Ara-Aralie",
}

for key in data:
    print (f"{key} : {data [key]}")

print ("\n --- batas --- \n")




# Lily JKT48 Profil Lengkap

data = {
    "nama" : "Hillary Abigail Mantiri",
    "panggilan" : "Lily",
    "team" : "Love",
    "tanggal" : "19 Oktober 2007",
    "tempat" : "Dover, New Hampshire, United States of America",
    "tinggi" : "163 cm",
    "tahun_aktif" : 2023,
    "member" : "Inti",
    "jikoshoukai" : "Papipapipum! Aku akan mengejutkanmu dengan kehebatanku. Halo, nama aku Lily.",
}

for key in data:
    print (f"{key} : {data [key]}")

print ("\n --- batas --- \n")

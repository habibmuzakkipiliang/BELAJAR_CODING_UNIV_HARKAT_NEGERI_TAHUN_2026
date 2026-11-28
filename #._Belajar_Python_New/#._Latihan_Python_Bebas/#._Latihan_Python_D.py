# Latihan Python

# Array Python

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

for y in daftar:
    print (y)

print ("\n --- batas --- \n")



# Daftar negara lain

negara = [
    "Indonesia",
    "Malaysia",
    "Singapura",
    "Thailand",
    "Myanmar",
    "Papua Nugini"
]

negara.append ("Palestina")
negara.append ("Eropa Timur")
negara.append ("Eropa Selatan")
negara.append ("Eropa Barat")
negara.append ("Eropa Utara")

for r in negara:
    print (r)


print ("\n --- batas --- \n")



# Dictionary 

data = {
    "kursi": 4000,
    "meja": 5000,
    "bangku": 9000,
    "ayam": 80000,
    "sayuran": 40000,
    "cabai": 90000,
    "susu": 5000,
    "kopi": 7000,
}

for key in data:
    print (f"{key} : {data [key]}")

print ("\n --- batas --- \n")



# Fungsi dasar 

def dasar ():
    print ("hello dasar")

dasar ()


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def halo (nama):
    print (f"Halo nama saya {nama} dari Jakarta Timur")

halo ("Rayyan")
halo ("Rubber")
halo ("Fun")
halo ("Ol")
halo ("Run")
halo ("Rub")


print ("\n --- batas --- \n")



# Fungsi return dengan dasar

def nama (halo):
    return f"Halo nama saya {halo} dari Jepang"

print (halo ("Rayyan"))
print (halo ("Ron"))
print (halo ("Run"))
print (halo ("Gun"))

print ("\n --- batas ---- \n")
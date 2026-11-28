flores = ["Aril", "Gibran", "Nikson", "Brian"]

for e in flores:
    if e == "Nikson":
        continue
    print (e)

print ("\n --- batas --- \n")


list_kota = [
    "jakarta",
    "bandung",
    "surabaya",
]

cari = input ("Masukkan kota :")

for kota in list_kota:
    if kota.lower() == cari.lower():
        print (f"Kota {cari.lower()} ditemukan")
        break

    else:
        print ("Kota tidak ditemukan")

print ("\n --- batas --- \n")
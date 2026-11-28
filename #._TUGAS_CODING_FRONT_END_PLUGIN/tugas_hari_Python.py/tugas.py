# Array Python

nilai_x = [20, 80, 90, 100, 70]

for h in nilai_x:
    print (h)


print ("\n --- batas --- \n")



# Percabangan (Konditional) Python

nilai_i = 70

if nilai_i > 100 or nilai_i < 0:
    print (f"Nilai A, nilai = {nilai_i}")

elif nilai_i >= 70 and nilai_i <= 80:
    print (f"Nilai B, nilai = {nilai_i}")

elif nilai_i >= 60 and nilai_i <= 70:
    print (f"Nilai C, nilai = {nilai_i}")

elif nilai_i == 60:
    print (f"Nilai E, nilai = {nilai_i}")

elif nilai_i < 60:
    print (f"Nilai dibawah E, nilai = {nilai_i}")

else:
    print (f"Input tidak valid, nilai = {nilai_i}")

print ("\n --- batas --- \n")




# Dictionary (Object)

biodata = {
    "nama" : "Habib Muzakki",
    "kelas" : "1B",
    "asal_daerah" : "Kota serang",
    "skill" : "HTMl, CSS, JavaScript dan Python",
    "marga" : "Piliang"
} 

for key in biodata:
    print (f"{key} : {biodata [key]}")


print ("\n --- batas --- \n")
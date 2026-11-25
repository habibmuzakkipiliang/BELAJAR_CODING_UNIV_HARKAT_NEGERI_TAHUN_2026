jawab = str (input ("masukkan ya / tidak = "))

while True:
    print ("Kamu memilih ya")
    jawab = str (input ("Masukkan iya / tidak = "))
    if jawab.lower() == "tidak":
        break

    print (f"Kamu memilih tidak")
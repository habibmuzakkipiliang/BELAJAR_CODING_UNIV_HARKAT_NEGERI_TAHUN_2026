jawab = str (input ("Masukkan ya/tidak = "))

while jawab.lower() == "ya":
    print ("Kamu memilih ya")
    jawab = input ("Masukkan iya / tidak = ")


print (f"Kamu memilih {jawab.lower()}")
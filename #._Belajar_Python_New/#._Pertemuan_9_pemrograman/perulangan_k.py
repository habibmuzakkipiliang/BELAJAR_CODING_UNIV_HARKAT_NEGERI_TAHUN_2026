print("\n================ KALKULATOR SEDERHANA ================\n")

while True:
    print("== Pilih Operasi ==")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan angka kamu sekarang (1 - 5) = ")

    if pilihan == "5":
        print("Terima kasih telah memilih program ini")
        break

    if pilihan in ["1", "2", "3", "4"]:
        a = float(input("Masukkan angka pertama = "))
        b = float(input("Masukkan angka kedua = "))

        if pilihan == "1":
            hasil = a + b
            operasi = "+"
        elif pilihan == "2":
            hasil = a - b
            operasi = "-"
        elif pilihan == "3":
            hasil = a * b
            operasi = "X"
        elif pilihan == "4":
            if b == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan\n")
                continue
            hasil = a / b
            operasi = "÷"

        print(f"\nHasil: {a} {operasi} {b} = {hasil}\n")
    else:
        print("Pilihan tidak valid! Silakan coba lagi\n")
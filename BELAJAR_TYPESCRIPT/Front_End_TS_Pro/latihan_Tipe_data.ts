// Tipe data pemrograman primitif

const nama_r : string = "Radit"
const umur : number = 19
const menikat : boolean = false

console.log (nama_r)
console.log (umur)
console.log (menikat)


// non primitif

const hobi: string[] = ["Ngidol JKT48", "Nonton Anime", "Suka oshi JKT48"]
const alamat: Record<string, any> = {
    jalan: "Jn Gatot Subroto",
    kota: "Jakarta",
    kode_pos: 12,
    kompleks : {
        nama: "Habib Muzakki",
        kelas: "1B",
    },

    anggota_keluarga: ["Ayah", "Ibu", "Anak"]
}

console.log (alamat.anggota_keluarga[0])

console.log ("\n --- batas --- \n")
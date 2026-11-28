console.log ("Hello World")

console.log ("\n --- batas --- \n")


let teks : string = "Halo Dunia"
let angka : number = 12
let desimal : number = 12.2
let cek : boolean = true

console.log (teks)
console.log (angka)
console.log (desimal)
console.log (cek)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

let teksU : string = "Halo Dunia"
let angkaU : number = 12
let desimalU : number = 12.1
let cekU : boolean = true

let tipe = `
\n Teks     : ${teksU}
\n Angka    : ${angkaU}
\n Desimal  : ${desimalU}
\n Cek      : ${cekU}

`

console.log (tipe)

console.log ("\n --- batas --- \n")



// Cek tipe data pemrograman

console.log ("Teks =", typeof (teksU))
console.log ("Angka =", typeof (angkaU))
console.log ("Desimal =", typeof (desimalU))
console.log ("Cek =", typeof (cekU))


console.log ("\n --- batas --- \n")



// Fungsi return dengan operasi dasar

let xU : number = 12
let yU : number = 5

function tambah (xU : number, yU : number) {
    return xU + yU
}

function kurang (xU : number, yU : number) {
    return xU - yU
}

function kali (xU : number, yU : number) {
    return xU * yU 
}

function pangkat (xU : number, yU: number) {
    return xU ** yU
} 


console.log ("Tambah =", tambah (xU, yU))
console.log ("Kurang =", kurang (xU, yU))
console.log ("Kali =", kali (xU, yU))
console.log ("Pangkat =", pangkat (xU, yU))


console.log ("\n --- batas --- \n")




// Percabangan dasar 

let angka_1 : number = 12

if (angka_1 >= 8) {
    console.log (`Angka besar, angka 1 = ${angka_1}`)
}

else {
    console.log (`Angka kecil, angka 1 = ${angka_1}`)
}


console.log ("\n --- batas --- \n")



// Percabangan Lanjutan 

let angka_2 : number = -5

if (angka_2 > 0) {
    console.log (`angka positif, angka 2 = ${angka_2}`)
}

else if (angka_2 < 0) {
    console.log (`angka negatif, angka 2 = ${angka_2}`)
}

else {
    console.log (`angka nol, angka 2 = ${angka_2}`)
}


console.log ("\n --- batas --- \n")



// Percabangan pemilihan film bioskop dan usia kamu sekarang

let usia_kamu : number = 19
let genre_bioskop : string = "horor"
let cek_1 : boolean = cek

if (genre_bioskop == "action") {
    if (usia_kamu >= 13 && usia_kamu <= 19) {
        if (cek_1) {
            console.log (`kamu boleh nonton bioskop, usia kamu = ${usia_kamu} dan genre bioskop = ${genre_bioskop}`)
        }

        else {
            console.log (`kamu jangan nonton dulu, usia kamu = ${usia_kamu} dan genre film = ${genre_bioskop}`)
        }
    }
}

else if (genre_bioskop == "horor") {
    if (usia_kamu >= 19 && usia_kamu <= 19) {
        console.log (`Kamu boleh nonton, usia kamu = ${usia_kamu} dan genre film = ${genre_bioskop}`)
    }

    else {
        console.log (`Jangan nonton dulu film horor, usia kamu = ${usia_kamu} dan genre film = ${genre_bioskop}`)
    }
}

else if (genre_bioskop == "kartun") {
    if (usia_kamu >= 2 && usia_kamu <= 10) {
        console.log (`boleh nonton film kartun, usia kamu = ${usia_kamu} dan genre film = ${genre_bioskop}`)
    }

    else {
        console.log (`jangan nonton kartum, usia kamu = ${usia_kamu} dan genre film = ${genre_bioskop}`)
    }
}

else {
    console.log (`input tidak valid, usia kamu = ${usia_kamu} dan genre film = ${genre_bioskop}`)
}

console.log ("\n --- batas --- \n")



// Percabangan usia manusia 

let usia_jun : number = 30
let statuk_jun : string = "tua"

if (statuk_jun == "tua") {
    if (usia_jun >= 50 && usia_jun <= 80) {
        console.log (`usia kamu sudah tua, usia kamu = ${usia_jun} dan statuk = ${statuk_jun}`)
    }
}

else if (statuk_jun === "dewasa") {
    if (usia_jun >= 25 && usia_jun <= 49) {
        console.log (`masuk dewasa, usia kamu = ${usia_jun} dan statuk kamu = ${statuk_jun}`)
    }

    else {
        console.log (`berarti kamu bukan dewasa, usia kamu = ${usia_jun} dan statuk kamu = ${statuk_jun}`)
    }
}
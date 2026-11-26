console.log ("Hello World")


console.log ("\n --- batas --- \n")



// variabel dasar

var a = "Hello World"
var b = "Halo Fansbase"
var c = 12
var d = 3.22

console.log (a)
console.log (b)
console.log (c)
console.log (d)


console.log ("\n --- batas --- \n")


// Fungsi return dengan operator dasar

var x = 10
var y = 5

function tambah (x, y) {
    return x + y
}

function kurang (x, y) {
    return x - y
}

function kali (x, y) {
    return x * y
}

function pangkat (x, y) {
    return x ** y
}

function bagi (x, y) {
    return x / y
}

function modulus (x, y) {
    return x % y
}

console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))
console.log ("Modulus =", modulus (x, y))


console.log ("\n --- batas --- \n")



// Percabangan dasar 

var angka = 12

if (angka >= 8) {
    console.log (`besar, angka = ${angka}`)
}

else {
    console.log (`kecil, angka = ${angka}`)
}


console.log ("\n --- batas --- \n")




// Percabangan lanjutan 

var angka = -10

if (angka > 0) {
    console.log (`Angka positif, angka = ${angka}`)
}

else if (angka < 0) {
    console.log (`Angka negatif, angka = ${angka}`)
}

else {
    console.log (`Angka nol, angka = ${angka}`)
}


console.log ("\n --- batas --- \n")



// Percabangan nested pemilihan genre video youtube dan usia kamu sekarang

genre = "horor"
usia = 19
cek = true

if (genre == "horor") {
    if (usia >= 18 && usia <= 19) {
        if (cek) {
            console.log (`boleh nonton film horor di youtube, usia = ${usia} dan genre video = ${genre}`)
        }
    }

    else {
        console.log (`jangan nonton dulu di youtube, usia = ${usia} dan genre video = ${genre}`)
    }
}

else if (genre == "kartun") {
    if (usia >= 5 && usia <= 19) {
        console.log (`boleh nonton film kartun, usia = ${usia} dan genre video = ${genre}`)
    }

    else {
        console.log (`jangan nonton dulu, usia = ${usia} dan genre video = ${genre}`)
    }
}

else if (genre == "komedi") {
    if (usia >= 18 && usia <= 19) {
        console.log (`boleh nonton video komedi, usia = ${usia} dan ${genre}`)
    }

    else {
        console.log (`jangan nonton video komedi, usia = ${usia} dan genre video = ${genre}`)
    }
}

else if (genre == "idol") {
    if (usia >= 20 && usia <= 30) {
        console.log (`boleh nonton video idol, usia = ${usia} dan genre video = ${genre}`)
    }

    else {
        console.log (`jangan nonton dulu video nya, usia = ${usia} dan genre video = ${genre}`)
    }
}

else {
    console.log (`input tidak valid, usia = ${usia} dan genre video = ${genre}`)
}


console.log ("\n --- batas --- \n")



// percabangan pemilihan jenjang pendidikan manusia

pendidikan = "kuliah"
usia = 19
cek = true

if (pendidikan == "kuliah") {
    if (usia >= 19 && usia <= 24) {
        if (cek) {
            console.log (`masuk kuliah, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
        }

        else {
            console.log (`bukan anak kuliahan, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
        }
    }
}

else if (pendidikan == "sma") {
    if (usia >= 16 && usia <= 18) {
        console.log (`masuk sma, usia kamu = ${usia} dan pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan sma, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }
}

else if (pendidikan == "smp") {
    if (usia >= 13 && usia <= 15) {
        console.log (`masuk smp, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan smp, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }
}

else if (pendidikan == "sd") {
    if (usia >= 6 && usia <= 12) {
        console.log (`masuk sd, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }

    else {
        console.log (`bukan sd, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }
}

else if (pendidikan == "tk") {
    if (usia >= 3 && usia <= 5) {
        console.log (`masuk tk, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }

    else {
        conssole.log (`bukan tk, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
    }
}

else {
    console.log (`input tidak valid, usia kamu = ${usia} dan jenjang pendidikan = ${pendidikan}`)
}


console.log ("\n --- batas --- \n")




// percabangan usia manusia 

var usia = 19
var statuk = "remaja"
var cek = true

if (statuk == "balita") {
    if (usia >= 1 && usia <= 4) {
        if (cek) {
            console.log (`berarti usia kamu balita, usia kamu = ${usia} dan statuk = ${statuk}`)
        }

        else {
            console.log (`bukan anak balita, usia kamu = ${usia} dan statuk = ${statuk}`)
        }
    }
}

else if (statuk == "anak-anak") {
    if (usia >= 5 && usia <= 12) {
        console.log (`anak-anak, usia kamu = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia anak-anak, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "remaja") {
    if (usia >= 14 && usia <= 19) {
        console.log (`usia kamu masuk remaja, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia remaja, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "dewasa") {
    if (usia >= 20 && usia <= 45) {
        console.log (`usia kamu sudah dewasa, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia dewasa, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else if (statuk == "tua") {
    if (usia >= 46 && usia <= 80) {
        console.log (`usia kamu sudah tua, usia = ${usia} dan statuk = ${statuk}`)
    }

    else {
        console.log (`bukan usia sudah tua, usia = ${usia} dan statuk = ${statuk}`)
    }
}

else {
    console.log (`input tidak valid, usia = ${usia} dan statuk = ${statuk}`)
}


// For dasar 

for (a = 0; a < 30; a++) {
    console.log ("Invofest adalah acara terbaik")
}

console.log ("\n --- batas --- \n")



// For dasar 

for (r = 0; r < 80; r++) {
    console.log ("aku ingin jadi ahli IT")
}

console.log ("\n --- batas --- ")


// For dasar 2

for (b = 0; b < 100; b++) {
    console.log ("Aku anak UHN Tegal")
}

console.log ("\n --- batas --- \n")


// For nested

for (a = 0; a < 10; a++) {
    for (b = 0; b < 10; b++) {
        for (c = 0; c < 10; c++) {
            console.log (`Halo saya Habib Muzaki dari D4 Vokasi Teknik Informatika ${a}`)
            console.log (`Halo saya suka dengan JKT48 ${b}`)
            console.log (`Halo saya suka dengan Invofest Harkat Negeri ${c}`)
        }
    }
}

console.log ("\n --- batas --- \n")



// For Nested 

for (x = 0; x < 15; x++) {
    for (y = 0; y < 15; y++) {
        for (z = 0; z < 15; z++) {
            console.log (`Halo Prof.Esther cantik ${x}`)
            console.log (`Halo Kak Jessica cantika ${y}`)
            console.log (`Halo kak, saya dari D4 Teknik Infortika ${z}`)
        }
    }
}

console.log ("\n --- batas --- \n")
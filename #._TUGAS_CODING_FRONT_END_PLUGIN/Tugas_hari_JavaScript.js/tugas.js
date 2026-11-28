// Array JavaScript

nilai_x = [20, 80, 90, 100, 70]

for (a = 0; a < nilai_x.length; a++) {
    console.log (nilai [a])
}

console.log ("\n --- batas --- \n")



// Percabangan (Konditional) JavaScript

nilai_i = 70

if (nilai_i > 100 || nilai_i < 0) {
    console.log (`Nilai A, nilai = ${nilai_i}`)
}

else if (nilai_i >= 70 && nilai_i <= 80) {
    console.log (`Nilai B, nilai = ${nilai_i}`)
}

else if (nilai_i >= 60 && nilai_i <= 70) {
    console.log (`Nilai C, nilai = ${nilai_i}`)
}

else if (nilai_i == 60) {
    console.log (`Nilai E, nilai = ${nilai_i}`)
}

else if (nilai_i < 60) {
    console.log (`Nilai E kebawah, nilai = ${nilai_i}`)
}

else {
    console.log (`Input tidak valid, nilai = ${nilai_i}`)
}


console.log ("\n --- batas --- \n")



// Object Biasa

var biodata = {
    "nama" : "Habib Muzakki",
    "kelas" : "1B",
    "asal_daerah" : "Kota serang",
    "skill" : "HTMl, CSS, JavaScript dan Python",
    "marga" : "Piliang"
}

for (var key in biodata) {
    console.log (`${key} : ${biodata [key]}`)
}


console.log ("\n --- batas --- \n")
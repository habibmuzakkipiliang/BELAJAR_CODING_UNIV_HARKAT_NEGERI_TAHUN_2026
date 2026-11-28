// Array TypeScript

const nilai_x : number[] = [20, 80, 90, 100, 70]

for (let x = 0; x < nilai_x.length; x++) {
    console.log (nilai_x [x])
}

console.log ("\n --- batas --- \n")



// Percabangan (Konditional) TypeScript

let nilai_i : number = 70

if (nilai_i > 100 || nilai_i < 0) {
    console.log (`Nilai A, nilai = ${nilai_i}`)
}

else if (nilai_i >= 70 && nilai_i <= 80) {
    console.log (`Nilai B, nilai = ${nilai_i} `)
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
    console.log (`input tidak valid, nilai = ${nilai_i}`)
}


console.log ("\n --- batas --- \n")



//  Object Biasa TypeScript

let biodata : Record <string, any> = {
    "nama" : "Habib Muzakki",
    "kelas" : "1B",
    "asal_daerah" : "Kota serang",
    "skill" : "HTMl, CSS, JavaScript dan Python",
    "marga" : "Piliang"
}

for (let key in biodata) {
    console.log (`${key} : ${biodata [key]}`)
}

console.log ("\n --- batas --- \n")
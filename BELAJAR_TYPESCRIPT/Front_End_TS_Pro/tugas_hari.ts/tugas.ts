// Array

const nilai_x : number[] = [20, 80, 90, 100, 70]

for (let x = 0; x < nilai_x.length; x++) {
    console.log (nilai_x [x])
}

console.log ("\n --- batas --- \n")



let nilai_i : number = 90

if (nilai_i >= 90 && nilai_i <= 100) {
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



//  Object Biasa

let biodata : Record <string, any> = {
    "nama" : "Habib Muzakki",
    "kelas" : "1B",
    "asal_daerah" : "Kota serang",
    "skill" : "HTMl, CSS, JavaScript dan Python",
    "marga" : "Piliang"
}

console.log ("Nama :", biodata.nama)
console.log ("Kelas :", biodata.kelas)
console.log ("Asal daerah :", biodata.asal_daerah)
console.log ("Skill :", biodata.skill)
console.log ("Marga :", biodata.marga)


console.log ("\n --- batas --- \n")
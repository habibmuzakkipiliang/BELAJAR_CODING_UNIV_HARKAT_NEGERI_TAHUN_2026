const nilai : number = 80

if (nilai === 90) {
    console.log (`Nilai kamu A, nilai = ${nilai}`)
}

else if (nilai === 80) {
    console.log (`Nilai kamu B, nilai = ${nilai}`)
}

else if (nilai === 70) {
    console.log (`Nilai kamu C, nilai = ${nilai}`)
}

else if (nilai === 60) {
    console.log (`Nilai kamu D, nilai = ${nilai}`)
}

else if (nilai === 50) {
    console.log (`Nilai kamu E, nilai = ${nilai}`)
}

else {
    console.log (`Input tidak valid, nilai = ${nilai}`)
}

if (nilai === 90) {
    if (nilai % 2 === 0) {
        console.log (`Nilai : ${nilai} | Genap`)
    }

    else {
        console.log (`Nilai : ${nilai} | Ganjil`)
    }
}
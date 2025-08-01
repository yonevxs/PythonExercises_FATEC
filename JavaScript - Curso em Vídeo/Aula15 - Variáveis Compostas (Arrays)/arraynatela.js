let values = [8, 1, 7, 4, 2, 9]

// for(let i = 0; i < values.length; i++){
//     console.log(`A posição ${i} tem o valor ${values[i]}`)
// }

//Para cada posição(POS) dentro de VALUES
for(let pos in values){
    console.log(`A posição ${pos} tem o valor ${values[pos]}`)
}

let pos = values.indexOf(2)
if(pos == -1){
    console.log('O valor não foi encontrado!')
} else{
    console.log(`O valor 2 está na posição ${pos}`)
}
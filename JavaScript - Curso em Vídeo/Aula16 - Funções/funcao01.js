function parImpar(n){ //Parâmetro formal
    if(n % 2 == 0){
        return 'Par!'
    } else{
        return 'Impar!'
    }
}
let res = parImpar(4) //Parâmetro real
console.log(res)

//Chamando função sem guardar o resultado em uma variável
console.log(parImpar(223))
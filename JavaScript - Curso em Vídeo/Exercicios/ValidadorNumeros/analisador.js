let num = document.getElementById('numtxt')
let lista = document.querySelector('select#listanum')
let res = document.querySelector('div#res')
let numList = []

function isNumero(n){
    if(Number(n) >= 1 && Number(n) <= 100){
        return true
    } else{
        return false
    }
}

function inLista(n, l){
    if(l.indexOf(Number(n)) != -1){
        return true
    } else{
        return false
    }
}

function adicionar(){
    //Adicionando caso for um número e não estiver na Lista
    if(isNumero(num.value) && !inLista(num.value, numList)){
        numList.push(Number(num.value))

        let option = document.createElement('option')
        option.text = `Valor ${num.value} adicionado.`
        lista.appendChild(option)
        res.innerHTML = ''
    } else{
        alert('[ERRO] - Valor inválido ou já encontrado na lista!')
    }

    //Apagando valores da caixa de texto após adicionar
    num.value = ''
    num.focus()
    
}

function finalizar(){
    if(numList.length == 0){
        alert('Adicione valores à lista antes de finalizar!')
    } else{
        let total = numList.length
        let maior = numList[0]
        let menor = numList[0]
        let soma = 0
        let media = 0

        for(let posicao in numList){
            soma += numList[posicao]
            if(numList[posicao] > maior){
                maior = numList[posicao]
            }
            if(numList[posicao] < menor){
                menor = numList[posicao]
            } 
        }
        media = soma / total
        res.innerHTML = ''
        res.innerHTML += `<p> Ao todo, temos ${total} números cadastrados`
        res.innerHTML += `<p> O maior valor informado foi ${maior}`
        res.innerHTML += `<p> O menor valor informado foi ${menor}`
        res.innerHTML += `<p> Somando todos os valores, temos ${soma}`
        res.innerHTML += `<p> A média dos valores digitados é ${media.toFixed(2).replace('.', ',')}`
    }
}
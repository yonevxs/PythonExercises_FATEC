function contar(){
    let inputInicio = document.getElementById('contInicio')
    let inputFim = document.getElementById('contFim')
    let inputPasso = document.getElementById('contPasso')
    let res = document.querySelector('div#res')

    if(inputInicio.value.length == 0 || inputFim.value.length == 0 || inputPasso.value.length == 0){
        res.innerHTML = 'Impossível contar'
        alert('[ERRO] - Faltam dados!')
    } else{
        res.innerHTML = 'Contando: <br>'
        let i = Number(inputInicio.value)
        let f = Number(inputFim.value)
        let p = Number(inputPasso.value)

        if(p == 0){
            window.alert('Passo inválido! Considerando PASSO = 1')
            p = 1
        }

        if(i < f){
            for(let c = i; c <= f; c += p){
                //Formatação de emojis em JS - U+1F603 = \u{1F603}
                res.innerHTML += ` ${c} \u{1F449}`
            }
            //Código UNICODE só funciona entre craser
            res.innerHTML += `\u{1F3C1}`
        } else{
            for(let c = i; c >= f; c -= p){
                res.innerHTML += ` ${c} \u{1F449}`
            }
            res.innerHTML += `\u{1F3C1}`
        }
    }
    
}
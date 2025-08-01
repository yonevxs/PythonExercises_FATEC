function tabuada(){
    let num = document.getElementById('txtn')
    let tab = document.getElementById('seltab')

    if(num.value.length == 0){
        alert('Digite um número!')
    } else{
        let n = Number(num.value)
        let c = 1
        //Antes de começar uma tabuada, você irá limpar a anterior
        tab.innerHTML = ''
        while(c <= 10){
            //Criando um elemento "option" para ser inserido dentro do elemento "select"
            let item = document.createElement('option')
            //Adicionando value ao elemento option
            item.value = `tab${c}`
            //Criando texto dentro do "option"
            item.text = `${n} x ${c} = ${n * c}`
            //Adicionando elemento filho (item) ao tab
            tab.appendChild(item)
            c++
        }
    }
}
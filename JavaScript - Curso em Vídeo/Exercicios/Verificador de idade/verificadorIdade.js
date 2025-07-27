function check(){
    let data = new Date()
    let ano = data.getFullYear()
    let anoUser = document.getElementById('txtnasc')
    let res = document.querySelector('div#res')

    //Pegando caracteres de String e o valor da String
    if(anoUser.value.length == 0 || Number(anoUser.value) > ano || Number(anoUser).value == 0){
        alert('[ERRO] - Verifique os dados e tente novamente')
    } else{
        let sex = document.getElementsByName('radsex')
        let idade = ano - Number(anoUser.value)
        let genero = ''

        //Criando um img dinamincamente - Dentro do JS
        let img = document.createElement("img")
        //Criando um id para a tag img -> 'tipo de atributo', 'nome para o atributo'
        img.setAttribute("id", "foto")

        //Verifica qual sexo foi selecionado
        if(sex[0].checked){
            genero = 'Homem'
            if(idade >= 0 && idade < 10){
             img.setAttribute('src', 'img/kid-man.jpg')

            } else if (idade <= 21){
                img.setAttribute('src', 'img/young-man.jpg')

            } else if(idade < 50){
                img.setAttribute('src', 'img/adult-man.jpg')

            } else{
                img.setAttribute('src', 'img/old-man.jpg')

            }
        } else if(sex[1].checked){
            genero = 'Mulher'
            if(idade >= 0 && idade < 10){
             img.setAttribute('src', 'img/kid-woman.jpg')
            } else if (idade <= 21){
                img.setAttribute('src', 'img/young-woman.jpg')
            } else if(idade < 50){
                img.setAttribute('src', 'img/adult-woman.jpg')
            } else{
                img.setAttribute('src', 'img/old-woman.jpg')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos`

        //Adicionando um elemento via JS
        res.appendChild(img)
    }
}
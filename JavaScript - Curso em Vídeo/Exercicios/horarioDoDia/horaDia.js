function carregar(){
    let msg = document.getElementById('msg')
    let img = document.getElementById('img')
    let data = new Date()
    let hora = data.getHours()
    let min = data.getMinutes()

    msg.innerHTML = `<strong>Agora são ${hora}:${min}h</strong>`

    if(hora >= 0 && hora < 12){
        msg.innerHTML += '<br><strong>Bom dia!</strong>'
        document.body.style.background = 'linear-gradient(180deg, #fcff9e, #d9dd66ff, #c67700 90%) no-repeat fixed'
        img.src = 'imgs/foto-manha.png'
    } else if(hora >= 12 && hora < 18){
        msg.innerHTML += '<br><strong>Boa tarde!</strong>'
        document.body.style.background = 'linear-gradient(0deg, #ee6a12ff 0%, #daae51 100%) no-repeat fixed'
        img.src = 'imgs/foto-tarde.jpg'
    } else{
        msg.innerHTML += '<br><strong>Boa noite!</strong>'
        document.body.style.background = 'linear-gradient(180deg, #3F2B96 0%, #809ce2ff 100%) no-repeat fixed'
        img.src = 'imgs/foto-noite.jpg'
    }
}

let button = document.getElementById('dark')
button.addEventListener('click', darkmode)

function darkmode(){
    document.body.style.background = '#212241ff'

    let h1 = document.getElementsByTagName('h1')[0]
    h1.style.color = '#dedee9ff'
    
    let p1 = document.getElementsByTagName('p')[0]
    p1.style.color = '#dedee9ff'

    document.body.addEventListener('dblclick', carregar)
    document.body.addEventListener('dblclick', function(){
        h1.style.color = '#212022ff'
        p1.style.color = '#212022ff'
    })
    
}
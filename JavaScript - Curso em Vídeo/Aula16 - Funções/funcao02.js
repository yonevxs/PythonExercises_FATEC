// Impedindo erro NaN
// Caso eu não passe um dos valores no parâmetro, ele vira zero.
function soma(n1=0, n2=0){
    return n1 + n2;
}

console.log(soma(7))
const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout,
    });

readline.question('Digite algo: ', (resposta) => {
      console.log(`Você digitou: ${resposta}`);
      readline.close();
    });

/*var c = 1
do{
    console.log(`Passo ${c}`)
    c++
} while(c <= 4)*/


/*var c = 1
while(c <= 3){
    console.log(`Passo ${c}`)
    c++ // c = c + 1
}*/

/*console.log('Tudo bem?')
console.log('Tudo bem?')
console.log('Tudo bem?')
console.log('Tudo bem?')
console.log('Tudo bem?')
console.log('Tudo bem?')
console.log('Tudo bem?')
console.log('Tudo bem?')*/
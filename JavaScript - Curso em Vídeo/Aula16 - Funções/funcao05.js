//Função recursiva
function fatorial(n){
    if(n == 1){
        return 1
    } else{
        return n * fatorial(n-1)
    }
}

console.log(fatorial(5))
/*

5! = 5 * 4 * 3 * 2 * 1
4! é 4 * 3 * 2 * 1, logo 5! = 5 * 4!

O fatorial de um número pode ser cálculado pelo fatorial de outro
n! = n * (n-1)!

1! = 1
*/
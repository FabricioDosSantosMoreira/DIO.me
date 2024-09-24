function somaNumeros(arr) {
    return arr.reduce(function(prev, current) {
        return prev + current;
    });
}

const nums = [1, 2, 3, 4];
console.log(nums);
console.log(somaNumeros(nums));



const lista = [
    {
        name: 'A',
        preco: 10,
    }, 
    {
        name: 'B',
        preco: 20,
    }, 
    {
        name: 'C',
        preco: 30,
    }, 
];

const saldoDisponivel = 100;

function calculaSaldo(saldoDisponivel, lista) {
    return lista.reduce(function(prev, current) {
        return prev - current.preco;
    }, saldoDisponivel);
}

console.log('\n\n', lista);
console.log(calculaSaldo(saldoDisponivel, lista));

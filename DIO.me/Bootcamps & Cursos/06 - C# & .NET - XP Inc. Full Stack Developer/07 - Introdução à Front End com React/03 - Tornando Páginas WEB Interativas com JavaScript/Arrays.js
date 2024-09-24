
const numeros = [10, 25, 40, 74, 35];

const letras = ['a', 'b', 'c', 'd'];

const estados = [
    {nome: 'Rio Grande do Sul', sigla: 'RS'},
    {nome: 'Santa Catarina', sigla: 'SC'}
]
estados.push({nome: 'São Paulo', sigla: 'SP'});
estados.push({nome: 'Rio de Janeiro', sigla: 'RJ'});

estados.push({nome: 'Inválido', sigla: '-'});
estados.pop();

estados.forEach(val => {console.log(val)});


console.log("\nUsando o Filter:");
const estadosFiltrados = estados.filter(estado => estado.nome.includes('u'));
console.table(estadosFiltrados);


console.log("\nUsando o Find:");
const estadoRS = estados.find(estado => estado.sigla == 'RS');
console.log(estadoRS);


console.log("\nUsando o FindIndex:");
const indexRS = estados.findIndex(estado => estado.sigla == 'RS');
console.log(indexRS);


console.log("\nUsando o Reduce:");
const todasAsSiglasJuntas = estados.reduce((acc, estado) => {
    return acc + estado.sigla;
}, '');
console.log(todasAsSiglasJuntas);



console.log("\nUsando o Some:");
const algumEstadoRS = estados.some(estados => estados.sigla == 'RS')
console.log(algumEstadoRS);


console.log("\nUsando o Every:");
const todasSiglasRS = estados.every(estados => estados.sigla == 'RS')
console.log(todasSiglasRS);

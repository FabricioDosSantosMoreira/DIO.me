// Funções
function soma(n1, n2) {
    return n1 + n2;
}

console.log(`Resultado = ${soma(5, 8)}`)


// Arrow Functions
const somar = (n1, n2) => {
    return n1 + n2;
}

const somar_curto = (n1, n2) => n1 + n2;

console.log(`Resultado = ${somar(5, 8)}`)
console.log(`Resultado = ${somar_curto(5, 8)}`)

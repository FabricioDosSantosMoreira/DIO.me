// For
for (let idx = 0; idx <= 10; idx++) {
    console.log(`idx = ${idx}`);
}

// While
console.log("\n");
let i = 0;
while (i <= 10) {
    console.log(`i = ${i}`);
    i++;
}

// ForEach
const array = [1, 2, 30, 80, 80];

array.forEach((val, idx) => {
    console.log(`idx = ${idx}, val=${val}`)
})


// Map
const array2 = [1, 2, 30, 80, 80];

const resultado = array2.map((val) => {
    return val * 2;
})

console.log(resultado);
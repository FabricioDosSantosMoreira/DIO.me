function filtraPares(arr) {
    return arr.filter(callback);
}

function callback(item) {
    return item % 2 === 0;
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

console.log(nums);
console.log(filtraPares(nums));

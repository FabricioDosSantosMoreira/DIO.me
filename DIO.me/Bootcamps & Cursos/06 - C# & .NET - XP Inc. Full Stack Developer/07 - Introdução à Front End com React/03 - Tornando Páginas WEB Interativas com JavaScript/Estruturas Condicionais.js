console.log(1 == 1);
console.log(1 == '1');
console.log(1 === '1');


console.log(1 != '2');
console.log(1 !== '2');



// Exemplo de variáveis de entrada
let idade = 20;
let temCarteira = true;
let temMultas = false;

// Estrutura condicional com operadores lógicos
if (idade >= 18 && temCarteira && !temMultas) {
    console.log("Você pode dirigir!");
} else if (idade >= 18 && temCarteira && temMultas) {
    console.log("Você pode dirigir, mas precisa resolver suas multas.");
} else if (idade >= 18 && !temCarteira) {
    console.log("Você precisa tirar a carteira de motorista.");
} else {
    console.log("Você ainda não pode dirigir.");
}

// Outro exemplo utilizando operador OU (||)
let clima = "chuvoso";
let temGuardaChuva = false;

if (clima === "ensolarado" || temGuardaChuva) {
    console.log("Você pode sair sem se molhar.");
} else {
    console.log("É melhor esperar a chuva passar.");
}


function getDayOfWeek(dayNumber) {
    let dayName;
  
    switch (dayNumber) {
      case 0:
        dayName = 'Domingo';
        break;
      case 1:
        dayName = 'Segunda-feira';
        break;
      case 2:
        dayName = 'Terça-feira';
        break;
      case 3:
        dayName = 'Quarta-feira';
        break;
      case 4:
        dayName = 'Quinta-feira';
        break;
      case 5:
        dayName = 'Sexta-feira';
        break;
      case 6:
        dayName = 'Sábado';
        break;
      default:
        dayName = 'Dia inválido';
        break;
    }
  
    return dayName;
  }
  
  // Teste da função
  const dayNumber = 3;
  console.log(`O dia da semana para o número ${dayNumber} é ${getDayOfWeek(dayNumber)}.`);
  

const nota = 9;

nota > 5 ? console.log("Aprovado") : console.log("Reprovado")

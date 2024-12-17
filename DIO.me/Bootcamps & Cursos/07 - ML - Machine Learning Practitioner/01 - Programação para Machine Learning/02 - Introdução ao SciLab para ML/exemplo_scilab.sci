// Parte 1: Cálculo da área do quadrado
lado = input("Informe a medida do lado de um quadrado: ", "string");
lado = evstr(lado); // Converte a entrada de string para número

if (lado > 0) then
    area = lado * lado;
    printf("\nA área do quadrado é: %f\n", area);
else
    printf("\nO valor informado é inválido\n");
end


// Parte 2: Avaliação da nota
nota = input("Informe a sua nota: ", "string");
nota = evstr(nota); // Converte a entrada de string para número

if (nota >= 6) then
    printf("\nVocê passou!\n");
    
    if (nota == 6) then
        printf("\nMas, você deve estudar mais!\n");
    end
else
    printf("\nVocê reprovou!\n");
end


// Parte 3: Operadores relacionais

// Operadores | Signnificado
//     ==     |  Igual a
//     ~=     |  Diferente de 
//     >      |  Maior que
//     >=     |  Maior ou igual a
//     <      |  Menor que
//     <=     |  Menor ou igual a
n1 = 10
n2 = 25

if (n1 > n2) then
    printf("n1 é maior que n2!")
end


// Operador Lógico OU - ||
bool maiorDeIdade = false;
bool possuiAutorizacao = true;


if (maiorDeIdade || possuiAutorizacao) 
{
    Console.WriteLine("Entrada Permitida!");
} 
else 
{
    Console.WriteLine("Entrada não permitida!");
}


// Operador Lógico AND - &&
bool possuiPresencaMinima = true;
double media = 6;

if (possuiPresencaMinima && media >= 7) 
{
    Console.WriteLine("Aprovado!");
}
else 
{
    Console.WriteLine("Reprovado!");
}


// Operador Lógico NOT !
bool choveu = true;
bool estaTarde = true;

if (!choveu && !estaTarde)
{
    Console.WriteLine("Vou pedalar");
}
else 
{
    Console.WriteLine("Vou pedalar em outro dia");
}

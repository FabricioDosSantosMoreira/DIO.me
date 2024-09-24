using Interfaces.Models;
using Interfaces.Interface;

// Calculadora calculadora = new();
ICalculadora calculadora = new Calculadora();

int x = 10;
int y = 5;

int soma = calculadora.Somar(x, y);
Console.WriteLine($"Resultado ['{x} + {y}'] = {soma}");

int subtracao = calculadora.Subtrair(x, y);
Console.WriteLine($"Resultado ['{x} - {y}'] = {subtracao}");

int multiplcacao = calculadora.Multiplicar(x, y);
Console.WriteLine($"Resultado ['{x} * {y}'] = {multiplcacao}");

int divisao = calculadora.Dividir(x, y);
Console.WriteLine($"Resultado ['{x} / {y}'] = {divisao}");


// Usando o Método padrão da Interface
double a = 4;
double b = 3;
double potencia = calculadora.Potencia(a, b);
Console.WriteLine($"Resultado ['{a} ^ {b}'] = {potencia}");
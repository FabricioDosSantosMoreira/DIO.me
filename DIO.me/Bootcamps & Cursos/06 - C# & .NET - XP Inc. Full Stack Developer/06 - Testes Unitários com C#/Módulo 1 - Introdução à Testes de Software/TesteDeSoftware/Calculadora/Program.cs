using Calculadora.Services;

CalculadoraImpl calculadora = new CalculadoraImpl();


int num1 = 5;
int num2 = 10;
Console.WriteLine($"{num1} + {num2} = {calculadora.Somar(num1, num2)}");

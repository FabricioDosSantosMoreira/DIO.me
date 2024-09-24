using System;

class Program
{
    static void Main(string[] args)
    {
        // Criando uma instância de ProgramaCliente e chamando o método Main dela
        ProgramaCliente programaCliente = new ProgramaCliente();
        programaCliente.Executar(); // Você pode criar um método "Executar" em ProgramaCliente em vez de chamar Main diretamente
    }
}





// // Estrutura de Repetição FOR
// Console.WriteLine("\n\nEstrutura FOR");

// int numero = 10;
// int pararNoNumero = -1;
// for (int i = 0; i <= 10; i++)
// {
//     if (pararNoNumero == i && pararNoNumero != -1) 
//     {
//         break;
//     }

//     Console.WriteLine($"{numero} * {i} = {numero * i}");
// }



// // Estrutura de Repetição WHILE
// Console.WriteLine("\n\nEstrutura WHILE");

// numero = 5;
// int contador = 0;
// while (contador <= 10)
// {
//     Console.WriteLine($"{numero} * {contador} = {numero * contador}"); 
//     contador++;

//     if (contador == 6) 
//     {
//         break;
//     }
// } 


// // Estrutura de Repetição DO WHILE
// Console.WriteLine("\n\nEstrutura DO WHILE");

// int soma = 0, num;

// do
// {
//     Console.Write("Digite um número (0 para parar): ");
//     num = Convert.ToInt32(Console.ReadLine());
//     soma += num;

// } while (num != 0);

// Console.WriteLine($"Soma de todos os números: {soma}");

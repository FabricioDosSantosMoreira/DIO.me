using System;

namespace OperadoresCondicionais
{
    public class OperadoresCondicionais
    {
        public static void Main(string[] args)
        {
            // IF aninhado
            int quantidadeCompra = 10;
            int quantidadeEstoque = 20;

            Console.WriteLine($"Quantidade em Estoque: {quantidadeEstoque}");
            Console.WriteLine($"Quantidade Compra: {quantidadeCompra}");

            if (quantidadeCompra == 0) 
            {
                Console.WriteLine("Compra Inválida!");
            }
            else if (quantidadeEstoque >= quantidadeCompra)
            {
                Console.WriteLine("Item Comprado!");
                quantidadeEstoque -= quantidadeCompra;
                Console.WriteLine($"Quantidade em Estoque: {quantidadeEstoque}");
                Console.WriteLine($"Quantidade Compra: {quantidadeCompra}");
            } 
            else
            {
                Console.WriteLine("Faltou Estoque!");
            }

            // Switch Case
            Console.Write("Digite uma letra: ");
            var letra = Console.ReadLine();
            
            switch (letra)
            {
                case "a": 
                case "e": 
                case "i": 
                case "o": 
                case "u":
                    Console.WriteLine("É uma vogal!");
                    break;
                default:
                    Console.WriteLine("Não é uma vogal!");
                    break;
            }
        }
    }
}

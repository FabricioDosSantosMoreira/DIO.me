using System;

namespace OperadoresCondicionais
{
    public class OperadoresCondicionais
    {
        public void VerificarEstoque()
        {
            int quantidadeCompra = 10;
            int quantidadeEstoque = 20;

            Console.WriteLine($"Quantidade em Estoque: {quantidadeEstoque}");
            Console.WriteLine($"Quantidade Compra: {quantidadeCompra}");

            if (quantidadeEstoque >= quantidadeCompra)
            {
                Console.WriteLine("Item Comprado!");
                quantidadeEstoque -= quantidadeCompra;
            }
            else
            {
                Console.WriteLine("Faltou Estoque!");
            }

            Console.WriteLine($"Quantidade em Estoque: {quantidadeEstoque}");
            Console.WriteLine($"Quantidade Compra: {quantidadeCompra}");
        }

        public static void Main(string[] args)
        {
            OperadoresCondicionais operadores = new OperadoresCondicionais();
            operadores.VerificarEstoque();
        }
    }
}

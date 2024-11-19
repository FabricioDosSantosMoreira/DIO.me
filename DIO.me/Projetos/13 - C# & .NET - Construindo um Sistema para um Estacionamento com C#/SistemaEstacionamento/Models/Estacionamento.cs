using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

namespace SistemaEstacionamento.Models
{
    public class Estacionamento
    {
        private decimal precoInicial = 0;
        private decimal precoPorHora = 0;
        private List<string> veiculos = new List<string>();

        public Estacionamento(decimal precoInicial, decimal precoPorHora)
        {
            this.precoInicial = precoInicial;
            this.precoPorHora = precoPorHora;
        }

        public void AdicionarVeiculo()
        {
            bool continuar = true;
            while(continuar)
            {
                Console.Write("\nDigite a placa do veículo para estacionar: ");
                string? placa = Console.ReadLine();

                if (string.IsNullOrWhiteSpace(placa) || string.IsNullOrEmpty(placa))
                {
                    Console.WriteLine("\nEntrada inválida!");
                }
                else
                {
                    Console.WriteLine($"\nVeículo com a placa ['{placa}'] foi adicionado.");
                    veiculos.Add(placa);
                    continuar = false;
                }
            } 
        }

        public void RemoverVeiculo()
        {   
            string? placa = string.Empty;
            bool continuar = true;
            while(continuar)
            {
                Console.Write("\nDigite a placa do veículo para saída: ");
                placa = Console.ReadLine();

                if (string.IsNullOrWhiteSpace(placa) || string.IsNullOrEmpty(placa))
                {
                    Console.WriteLine("\nEntrada inválida!");
                }
                else
                {
                    continuar = false;
                }
            }

            if (veiculos.Any(x => x.ToUpper() == placa.ToUpper()))
            {
                Console.Write("\nDigite a quantidade de horas que o veículo permaneceu estacionado: ");
                string? horas = Console.ReadLine();
                decimal valorTotal = precoInicial + precoPorHora * Convert.ToInt32(horas); 

                Console.WriteLine($"\nVeículo com a placa ['{placa}'] foi removido e o preço total foi de: R${valorTotal}");
                veiculos.Remove(placa);
            }
            else
            {
                Console.WriteLine("\nDesculpe, mas esse veículo não foi encontrado aqui!");
            }
        }
        
        public void ListarVeiculos()
        {
            if (veiculos.Any())
            {
                Console.WriteLine("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
                Console.WriteLine("|        Veículos estacionados        |");
                Console.WriteLine("+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+");

                foreach (string placa in veiculos)
                {
                    Console.WriteLine($"|  {placa}");
                }
            }
            else
            {
                Console.WriteLine("\nNão há veículos estacionados!");
            }
        }
    }
}
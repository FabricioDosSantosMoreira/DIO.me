using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetoPOO.Models
{
    public abstract class Smartphone
    {
        public string Numero { get; set; }
        private string Model { get; set; }
        private string IMEI { get; set; }
        private int Memoria { get; set; }

        public Smartphone(string numero, string model, string imei, int memoria)
        {
            Numero = numero;
            Model = model;
            IMEI = imei;
            Memoria = memoria;
        }

        public void Ligar() 
        {
            Console.WriteLine("\nLigando...");
        }

        public void ReceberLigacao() 
        {
            Console.WriteLine("\nRecebendo ligação...");
        }

        public abstract bool InstalarAplicativo(string nome);
    }
}
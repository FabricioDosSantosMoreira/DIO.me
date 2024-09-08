using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetoPOO.Models
{
    public class Iphone : Smartphone
    {
        public Iphone(string numero, string model, string imei, int memoria) : base(numero, model, imei, memoria) { }
        
        public override bool InstalarAplicativo(string nome)
        {
            Console.WriteLine($"\nInstalando aplicativo ['{nome}']");
            Console.WriteLine($"Instalação falhou!");
            return false;
        }
    }
}
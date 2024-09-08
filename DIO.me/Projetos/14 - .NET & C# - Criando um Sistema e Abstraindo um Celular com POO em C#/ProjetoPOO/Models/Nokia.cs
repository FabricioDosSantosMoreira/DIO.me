using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetoPOO.Models
{
    public class Nokia : Smartphone
    {
        public Nokia(string numero, string model, string imei, int memoria) : base(numero, model, imei, memoria) { }

        public override bool InstalarAplicativo(string nome)
        {
            Console.WriteLine($"\nInstalando aplicativo ['{nome}']");
            Console.WriteLine($"Aplicativo instalado com sucesso!");
            return true;
        }
    }
}
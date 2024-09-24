using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Threading.Tasks;

namespace ExemploTuplas.Models
{
    public class LeituraArquivo
    {
        public static (bool Sucesso, string[] Linhas, int NumeroLinhas) LerArquivo(string caminho) 
        {   
            try
            {
                string[] linhas = File.ReadAllLines(caminho);
                return (true, linhas, linhas.Count());
            }
            catch (Exception exc)
            {
                return (false, new string[0], 0);
            }
           
        }
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Excecoes.Models
{
    public class ExemploExcecao
    {
        public void Metodo1() 
        { 
            try
            {
                Metodo2(); 
            }
            catch (Exception exc)
            {
                Console.WriteLine("Exceção Tratada! - " + exc.Message);
            }
        }
        
        
        public void Metodo2() { Metodo3(); }
        public void Metodo3() { Metodo4(); }
        public void Metodo4() { throw new Exception("Ocorreu uma exceção"); }
    }
}

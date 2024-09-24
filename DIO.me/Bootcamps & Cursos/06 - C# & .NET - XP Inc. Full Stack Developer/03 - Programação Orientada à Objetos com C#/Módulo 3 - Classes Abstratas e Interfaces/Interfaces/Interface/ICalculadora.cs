using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Interfaces.Interface
{
    public interface ICalculadora
    {
        int Somar(int num1, int num2);
        int Subtrair(int num1, int num2);
        int Multiplicar(int num1, int num2);
        int Dividir(int num1, int num2);

        // Método Padrão da Interface, que é opcional para as classes que implementam ICalculadora
        double Potencia(double num1, double num2)
        {
            return Math.Pow(num1, num2);
        }
    }
}
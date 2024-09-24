using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Operadores_Aritmeticos.Models
{
    public class Calculadora
    {
        
        public static void Somar(int x, int y)
        {
            Console.WriteLine($"{x} + {y} = {x + y}");
        }

        public static void Subtrair(int x, int y)
        {
            Console.WriteLine($"{x} - {y} = {x - y}");
        }

        public static void Multiplicar(int x, int y)
        {
            Console.WriteLine($"{x} * {y} = {x * y}");
        }

        public static void Dividir(int x, int y)
        {
            Console.WriteLine($"{x} / {y} = {x / y}");
        }

        public static void Dividir(float x, float y)
        {
            Console.WriteLine($"{x} / {y} = {x / y}");
        }

        public static void Potencia(int x, int y)
        {
            double res = Math.Pow(x, y);
            Console.WriteLine($"{x}^{y} = {res}");
        }

        public static void RaizQuadrada(double x)
        {
            double res = Math.Sqrt(x);
            Console.WriteLine($"2√{x} = {res}");
        }

        public static void Incrementar(int x)
        {   
            x++;
            Console.WriteLine($"x + 1 ou (x++) = {x}");
        }

        public static void Decrementar(int x)
        {   
            x--;
            Console.WriteLine($"x - 1 ou (x--) = {x}");
        }
        
        public static void Seno(double angulo) 
        {
            double radiano = angulo * Math.PI / 180;
            double seno = Math.Sin(radiano);
            Console.WriteLine($"Seno de {angulo}° = {Math.Round(seno, 4)}");
        }

        public static void Coseno(double angulo) 
        {
            double radiano = angulo * Math.PI / 180;
            double coseno = Math.Cos(radiano);
            Console.WriteLine($"Coseno de {angulo}° = {Math.Round(coseno, 4)}");
        }

        public static void Tangente(double angulo) 
        {
            double radiano = angulo * Math.PI / 180;
            double tangente = Math.Tan(radiano);
            Console.WriteLine($"Tangente de {angulo}° = {Math.Round(tangente, 4)}");
        }
    }
}
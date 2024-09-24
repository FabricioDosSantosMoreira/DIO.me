using System;
using System.ComponentModel.Design;
using Excecoes.Models;

try
{
    string[] linhas = File.ReadAllLines("Arquivos/t/exto.txt");

    foreach (string linha in linhas)
    {
        Console.WriteLine(linha);
    }
}
catch (FileNotFoundException)
{
    Console.WriteLine($"Ocorreu um erro. Arquivo não encontrado.");
}
catch (DirectoryNotFoundException)
{
    Console.WriteLine($"Ocorreu um erro. Diretório não encontrado.");
}
catch (Exception exc)
{
    Console.WriteLine($"Ocorreu uma Exceção {exc.Message}");
}
finally
{
    Console.WriteLine("Bloco Finally executado, independente de sucesso ou falhas");
}





// Exceção Personalizada
Console.WriteLine("\n\n\nExceção Personalizada");
ExemploExcecao eExc = new ExemploExcecao();
eExc.Metodo1();

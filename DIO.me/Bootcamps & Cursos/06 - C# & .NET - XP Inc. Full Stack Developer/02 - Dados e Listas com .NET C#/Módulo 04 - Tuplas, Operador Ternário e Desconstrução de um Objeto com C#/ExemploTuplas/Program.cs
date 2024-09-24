using System.ComponentModel;
using System.Reflection.Metadata.Ecma335;
using ExemploTuplas.Models;

// Tuplas
(int Id, string Nome, string Sobrenome) tupla = (1, "Fabrício", "dos Santos Moreira");

Console.WriteLine($"Item 1: {tupla.Item1}");
Console.WriteLine($"Item 2: {tupla.Item2}");
Console.WriteLine($"Item 3: {tupla.Item3}");

Console.WriteLine($"Item 1: {tupla.Id}");
Console.WriteLine($"Item 2: {tupla.Nome}");
Console.WriteLine($"Item 3: {tupla.Sobrenome}");


// Outras maneiras de criar tuplas
ValueTuple<int, string, string, decimal> outroExemploDeTupla1 = (1, "Fabrício", "dos Santos Moreira", 1.85M);
var outroExemploDeTupla2 = Tuple.Create(1, "Fabrício", "dos Santos Moreira", 1.85M);



// (bool Sucesso, string[] Linhas, int NumeroLinhas) tuplaLeitura = LeituraArquivo.LerArquivo("/Arquivos/texto.txt");
var (sucesso, linhas, _) = LeituraArquivo.LerArquivo("Arquivos/texto.txt");
// OBS: O '_' descarta a informação

if (sucesso)
{
    
    Console.WriteLine($"\n\n\nNúmero de linha do arquivo: FOI DESCARTADO COM '_'");
    foreach (string linha in linhas)
    {
        Console.WriteLine($"\nLinha: {linha}");
    }
}
else
{
    Console.WriteLine($"\nNão foi possível ler o arquivo");
}





// Desconstrutor
Console.WriteLine($"\n\n\nDesconstrutor:");

Pessoa p1 = new Pessoa("Fabrício", "dos Santos Moreira", 19);

// Isso acessa o Método Deconstruct em Pessoa
(string nome, string sobrenome) = p1;

Console.WriteLine($"Nome Completo: {nome} {sobrenome}");



// IF Ternário
Console.WriteLine($"\n\n\nIF Ternário:");

int numero = 15;
bool ehPar = false;

ehPar = numero % 2 == 0;
Console.WriteLine($"O número {numero} é " + (ehPar ? "Par" : "Ímpar"));

string ehhPar = numero % 2 == 0 ? "Par" : "Ímpar";

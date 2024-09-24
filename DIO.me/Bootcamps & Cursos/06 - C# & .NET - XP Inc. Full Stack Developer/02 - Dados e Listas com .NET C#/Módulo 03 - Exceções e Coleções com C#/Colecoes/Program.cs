// Filas - Queue - FIFO (First In First Out)
using System.Collections;
using System.Linq.Expressions;

Console.WriteLine($"\n\n\nExemplo de Filas:");

Queue<int> fila = new Queue<int>();

fila.Enqueue(1);
fila.Enqueue(2);
fila.Enqueue(3);
fila.Enqueue(4);
fila.Enqueue(5);

Console.WriteLine($"\nExibindo a Fila:");
foreach (int item in fila)
{
    Console.WriteLine($"Item: {item}");
}


Console.WriteLine($"Removendo o Item: {fila.Dequeue()}");
Console.WriteLine($"Removendo o Item: {fila.Dequeue()}");
fila.Enqueue(10);
Console.WriteLine($"Removendo o Item: {fila.Dequeue()}");


Console.WriteLine($"\nExibindo a Fila:");
foreach (int item in fila)
{
    Console.WriteLine($"Item: {item}");
}


// Pilhas - Stack - LIFO (Last In First Out)
Console.WriteLine($"\n\n\nExemplo de Pilhas:");
Stack<int> pilha = new Stack<int>();

pilha.Push(1);
pilha.Push(2);
pilha.Push(3);
pilha.Push(4);
pilha.Push(5);


Console.WriteLine($"\nExibindo a Pilha:");
foreach (int item in pilha)
{
    Console.WriteLine($"Item: {item}");
}


Console.WriteLine($"Removendo o Item do topo: {pilha.Pop()}");
Console.WriteLine($"Removendo o Item do topo: {pilha.Pop()}");
pilha.Push(10);
Console.WriteLine($"Removendo o Item do topo: {pilha.Pop()}");


Console.WriteLine($"\nExibindo a Pilha:");
foreach (int item in pilha)
{
    Console.WriteLine($"Item: {item}");
}



// Dicionário - armazena chave-valor em valores únicos
Console.WriteLine($"\n\n\nExemplo de Dicionário:");

Dictionary<string, string> estados = new Dictionary<string, string>();

estados.Add("RS", "Rio Grande do Sul");
estados.Add("SC", "Santa Catarina");
estados.Add("RJ", "Rio de Janeiro");
estados.Add("SP", "São Paulo");

Console.WriteLine($"\nExibindo o Dicionário:");
foreach (KeyValuePair<string, string> item in estados)
{
    Console.WriteLine($"Chave: {item.Key}, Valor: {item.Value}. Item: {item}");
}

// Alterando
estados["RS"] = "RIO GRANDE DO SUL";
estados["SC"] = "SANTA CATARINA";

Console.WriteLine($"\nExibindo o Dicionário Após Alteração:");
foreach (KeyValuePair<string, string> item in estados)
{
    Console.WriteLine($"Chave: {item.Key}, Valor: {item.Value}");
}

// Removendo
estados.Remove("SP");
estados.Remove("RJ");
estados.Remove("ALGUM ESTADO"); // Remove() retorna False, pois a chave não existe!

Console.WriteLine($"\nExibindo o Dicionário Após Remoção:");
foreach (KeyValuePair<string, string> item in estados)
{
    Console.WriteLine($"Chave: {item.Key}, Valor: {item.Value}");
}


string chave = "RJ";
Console.WriteLine($"Verificando o elemento ['{chave}']");
if (estados.ContainsKey(chave)) 
{
    Console.WriteLine("Valor existente!");
} 
else
{
    Console.WriteLine("Valor inexistente!");
}
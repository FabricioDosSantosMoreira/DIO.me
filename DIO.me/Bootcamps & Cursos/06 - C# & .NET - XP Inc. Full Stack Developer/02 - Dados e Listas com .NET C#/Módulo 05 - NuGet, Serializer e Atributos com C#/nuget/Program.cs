// dotnet add package Newtonsoft.Json --version 13.0.3
using nuget.Models;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;

// Convertendo um Objeto em JSON
Console.WriteLine("\n\n\nConvertendo um Objeto em JSON");

DateTime dataAtual = DateTime.Now;

Venda venda1 = new Venda(1, "Lápis", 2.50M, dataAtual);
Venda venda2 = new Venda(2, "Caneta", 4.70M, dataAtual);

List<Venda> listaVendas = [];
listaVendas.Add(venda1);
listaVendas.Add(venda2);

string serializado = JsonConvert.SerializeObject(listaVendas, Formatting.Indented);

Console.WriteLine(serializado);

string currentDirectory = Directory.GetCurrentDirectory();
string? projectDirectory = Directory.GetParent(currentDirectory).Parent.Parent.FullName;

File.WriteAllText(projectDirectory + "/Arquivos/vendas.json", serializado);




// Convertendo um JSON em objeto
Console.WriteLine("\n\n\nConvertendo um JSON em objeto");

string arquivo = File.ReadAllText(projectDirectory + "/Arquivos/vendasDesformatada.json");
List<Venda> listaVendasObtida = JsonConvert.DeserializeObject<List<Venda>>(arquivo);

foreach (Venda venda in listaVendasObtida)
{
    Console.WriteLine($"Id: {venda.Id}, " + 
                    $"Produto {venda.Produto}, " + 
                    $"Preço: {venda.Preco}, " + 
                    $"Data: {venda.DataVenda:dd/MM/yyyy HH:mm}");
}

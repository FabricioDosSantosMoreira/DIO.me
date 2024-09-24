using ManipulandoValores.Models;
using System.Globalization;

Pessoa p1 = new Pessoa(nome: "Fabrício", sobrenome: "dos Santos Moreira", idade: 19);

Pessoa p2 = new Pessoa();
p2.Nome = "Nome";
p2.Sobrenome = "Sobrenome";
p2.Idade = 19;


Curso cursoDeingles = new Curso{
    Nome = "Inglês",
    Alunos = new List<Pessoa>()
};


cursoDeingles.AdicionarAluno(p1);
cursoDeingles.AdicionarAluno(p2);

cursoDeingles.ListarAlunos();

cursoDeingles.RemoverAluno(p2);
cursoDeingles.ListarAlunos();


// Formatando Valores Monetários
Console.WriteLine("\nFormatando Valores Monetários:");

CultureInfo.DefaultThreadCurrentCulture = new CultureInfo("en-US");
CultureInfo.DefaultThreadCurrentCulture = new CultureInfo("pt-BR");
//CultureInfo.DefaultThreadCurrentCulture = new CultureInfo("ja-JP");

decimal valorMonetario = 1282.50M;

Console.WriteLine($"{valorMonetario:C}");
Console.WriteLine($"{valorMonetario.ToString("C", CultureInfo.CreateSpecificCulture("en-US"))}");

// Formatação Personalizada
Console.WriteLine("\nFormatação Personalizada:");

Console.WriteLine($"{valorMonetario.ToString("C1")}");
Console.WriteLine($"{valorMonetario.ToString("C3")}");
Console.WriteLine($"{valorMonetario.ToString("C8")}");
Console.WriteLine($"{valorMonetario:C1}");
Console.WriteLine($"{valorMonetario:N1}");
Console.WriteLine($"{valorMonetario:N8}");

double porcentagem =.3421;
Console.WriteLine($"{porcentagem.ToString("P")}");

int numero = 1234567890;
Console.WriteLine(numero.ToString("##-##-##"));



// Formatando o tipo DateTime
Console.WriteLine("\nFormatando o tipo DateTime:");

// CultureInfo.DefaultThreadCurrentCulture = new CultureInfo("en-US"); // para o 'tt' em ToString()

DateTime data = DateTime.Now;
Console.WriteLine(data.ToString("dd/MM/yyyy HH:mm:ss - tt      [zzz]"));
Console.WriteLine(data.ToShortDateString());
Console.WriteLine(data.ToShortTimeString());



// Convertendo o DateTime
Console.WriteLine("\nConvertendo o DateTime");

DateTime dataDeString = DateTime.Parse("20/10/2020 00:00");
Console.WriteLine(dataDeString);


// TryParseExact com data válida
string dataEmString = "2022-04-18 20:00";
string formato = "yyyy-MM-dd HH:mm";
DateTime.TryParseExact(dataEmString, formato, CultureInfo.InvariantCulture, DateTimeStyles.None, out DateTime dataOut);

Console.WriteLine(dataOut);


// TryParseExact com data inválida
dataEmString = "2024-13-40 20:00";
formato = "yyyy-MM-dd HH:mm";
DateTime.TryParseExact(dataEmString, formato, CultureInfo.InvariantCulture, DateTimeStyles.None, out dataOut);

Console.WriteLine(dataOut);


dataEmString = "2024-12-15 20:00";
formato = "yyyy-MM-dd HH:mm";
bool sucesso = DateTime.TryParseExact(dataEmString, formato, CultureInfo.InvariantCulture, DateTimeStyles.None, out DateTime dataFormatada);
if (sucesso)
{
    Console.WriteLine($"Conversão com sucesso ['{sucesso}'] Data = {dataFormatada}"); 
}
else
{
    Console.WriteLine($"Data = {dataEmString} não é válida! "); 
}

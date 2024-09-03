
// Comparador de Atribuição
int a = 1;
int b = 4;

int c = a + b;

c = c + 5;
c += 5;

Console.WriteLine(c);



// Convertendo tipos (Casting)
int convertido = Convert.ToInt32("444");
Console.WriteLine(convertido);

convertido = int.Parse("423");
Console.WriteLine(convertido);
// NOTE: A diferença entre Parse e Convert está no tratamento de nulos.



// COnversão para String
int inteiro = 5;


string valor_str = Convert.ToString(inteiro);
Console.WriteLine(valor_str);
Console.WriteLine(inteiro.ToString());




// Cast Implícito
int abc = 5;
double abcd = abc;

Console.WriteLine($"Cast Implícito = {abcd}");

// Cast Explícito

// Isso não da pois o long ultrapassa o int
long valor_longo = long.MaxValue;
int valor_menor = (int) valor_longo;  //int valor_menor =  Convert.ToInt32(valor_longo);
Console.WriteLine($"Cast Explícito falho = {valor_menor}");




int valor_inteiro_que_cabe = int.MaxValue;
long longo_a_partir_de_int = valor_inteiro_que_cabe;
Console.WriteLine($"Cast Explícito normal = {longo_a_partir_de_int}");

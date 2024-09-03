{
string variavel_string = "valor";

int variavel_int = 1;
long variavel_long = 100000000L;
uint variavel__uint = 10000;
byte variavel_byte = 255;
ulong variavel_ulong = 13931231841L;

decimal variavel_decimal = 18080310M;
double variavel_double = 1.80;
float variavel_float = 10.1240F;

bool variavel_bool = true;

Console.WriteLine(variavel_string);
Console.WriteLine(variavel_int);
Console.WriteLine(variavel_long);
Console.WriteLine(variavel__uint);
Console.WriteLine(variavel_byte);
Console.WriteLine(variavel_ulong);
Console.WriteLine(variavel_decimal);
Console.WriteLine(variavel_double);
Console.WriteLine(variavel_double.ToString("0.00"));
Console.WriteLine(variavel_float);
Console.WriteLine(variavel_bool);



DateTime dataAtual = DateTime.Now;
Console.WriteLine(dataAtual);

dataAtual = DateTime.Now.AddDays(5);
Console.WriteLine(dataAtual);

string dataAtualString = DateTime.Now.ToString("dd/MM/yyyy - HH:mm");
Console.WriteLine(dataAtualString);

dataAtualString = DateTime.Now.ToString("dd/MM - HH:mm");
Console.WriteLine(dataAtualString);
}

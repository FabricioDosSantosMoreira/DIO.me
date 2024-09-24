// Array é uma estrutura de dados que armazena valores do mesmo tipo, com um tamanho fixo
// int[] newArray = new int[4] {1, 2, 3, 3};
// int[] arrayOmitido = new int[] {1, 2, 3, 4};
// int[] array = [1, 2, 3, 4];

int[] arrayInteiro = new int[3];
arrayInteiro[0] = 10;
arrayInteiro[1] = 20;
arrayInteiro[2] = 10;


// Percorrendo o Array com o FOR
Console.WriteLine("\nPercorrendo o Array com FOR");
for (int i = 0; i < arrayInteiro.Length; i++)
{
    Console.WriteLine($"Índice {i} - {arrayInteiro[i]}");    
}


// Percorrendo o Array com FOREACH
Console.WriteLine("\nPercorrendo o Array com FOREACH");

int contadorExterno = 0;
foreach (int valor in arrayInteiro)
{
    Console.WriteLine($"Índice {contadorExterno} - {valor}");    
    contadorExterno ++;
}


// Aumentando o Array de tamanho
Console.WriteLine("\nAumentando o Array de tamanho");

int[] arrayInteiroGrande = new int[3];
arrayInteiroGrande[0] = 10;
arrayInteiroGrande[1] = 20;
arrayInteiroGrande[2] = 10;

Array.Resize(ref arrayInteiroGrande, 10);

for (int i = 0; i < arrayInteiroGrande.Length; i++)
{
    Console.WriteLine($"Índice {i} - {arrayInteiroGrande[i]}");    
}


// Copiando um Array para outro
Console.WriteLine("\nCopiando um Array para outro");

int[] arrayOriginal = new int[3];
arrayOriginal[0] = 101;
arrayOriginal[1] = 202;
arrayOriginal[2] = 103;

int[] arrayCopiado = new int[arrayOriginal.Length * 3];
Array.Copy(arrayOriginal, arrayCopiado, arrayOriginal.Length);


for (int i = 0; i < arrayCopiado.Length; i++)
{
    Console.WriteLine($"Índice {i} - {arrayCopiado[i]}");    
}



// Listas é um Array melhorado, sem toda a complexidade de um Array
Console.WriteLine("\nListas");

List<string> listaString = new List<string>();
listaString.Add("RS");
listaString.Add("SC");
listaString.Add("RJ");

contadorExterno = 0;
foreach (string item in listaString)
{
    Console.WriteLine($"Índice {contadorExterno} - {item}");
    contadorExterno++;
}

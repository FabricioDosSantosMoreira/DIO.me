using SistemaEstacionamento.Models;

// Coloca o encoding para UTF8 para exibir acentuação
Console.OutputEncoding = System.Text.Encoding.UTF8;

decimal precoInicial = 0;
decimal precoPorHora = 0;

Console.WriteLine("\nSeja bem vindo ao sistema de estacionamento!");

Console.Write("\nInforme o preço inicial: ");
precoInicial = Convert.ToDecimal(Console.ReadLine());

Console.Write("\nInforme o preço por hora: ");
precoPorHora = Convert.ToDecimal(Console.ReadLine());

// Instânciando a classe Estacionamento
Estacionamento estacionamento = new Estacionamento(precoInicial, precoPorHora);


string opcao = string.Empty;
while (true)
{
    Console.WriteLine("\n\n\n");
    Console.WriteLine("+-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
    Console.WriteLine("| Opções  |           Ação            |");
    Console.WriteLine("+-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
    Console.WriteLine("|    1    |   Listagem de veículos    |");
    Console.WriteLine("|    2    |   Entrada de veículo      |");
    Console.WriteLine("|    3    |   Saída de veículo        |");
    Console.WriteLine("|    4    |   Encerrar Sistema        |");
    Console.WriteLine("+-=-=-=-=-+-=-=-=-=-=-=-=-=-=-=-=-=-=-+");
    Console.Write("\n- - -> Digite a sua opção: ");

    switch (Console.ReadLine())
    {
        case "1":
            estacionamento.ListarVeiculos();
            break;

        case "2":
            estacionamento.AdicionarVeiculo();
            break;

        case "3":
            estacionamento.RemoverVeiculo();
            break;

        case "4":
            Console.WriteLine("\nPrograma encerrado!");
            Environment.Exit(0);
            break;

        default:
            Console.WriteLine("\nOpção inválida!");
            break;
    }

    Console.Write("\nPressione uma tecla para continuar: ");
    Console.ReadLine();
}

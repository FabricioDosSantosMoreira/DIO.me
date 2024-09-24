using System;

class ProgramaCliente
{
    public void Executar()
    {
        string? opcao = "";
        bool exibirMenu = true;

        while (exibirMenu)
        {   
            //Console.Clear();
            Console.WriteLine("\n\n1 - Cadastrar cliente");
            Console.WriteLine("2 - Buscar cliente");
            Console.WriteLine("3 - Apagar cliente");
            Console.WriteLine("4 - Encerrar");
            Console.Write("Digite a sua opção: ");

            opcao = Console.ReadLine();

            switch (opcao)
            {
                case "1":
                    Console.WriteLine("\nCadastro de cliente");
                    break;
                case "2":
                    Console.WriteLine("\nBuscar cliente");
                    break;
                case "3":
                    Console.WriteLine("\nApagar cliente");
                    break;
                case "4":
                    exibirMenu = false;
                    // Environment.Exit(0);
                    break;
                default:
                    Console.WriteLine("\nOpção Inválida!");
                    break;
            }
        }
        Console.WriteLine("O programa se encerrou!");
    }
}

using Encapsulamento.Models;

ContaCorrente conta = new ContaCorrente(1);

conta.ExibirSaldo();
conta.Sacar(1000);
conta.Depositar(1000);


conta.ExibirSaldo();
conta.Sacar(1500);
conta.Depositar(500);


conta.Sacar(-1);
conta.Depositar(-1);
conta.Sacar(0);
conta.Depositar(0);


conta.ExibirSaldo();
conta.Sacar(1500);
conta.ExibirSaldo();
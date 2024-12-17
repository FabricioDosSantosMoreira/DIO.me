total = 0;

x = input("Digite o primeiro número: ");

while (x ~= 0)
    total = total + x;

    x = input("Digite o próximo número (0 para parar): ");
end

printf("A soma do números é: %d", total);

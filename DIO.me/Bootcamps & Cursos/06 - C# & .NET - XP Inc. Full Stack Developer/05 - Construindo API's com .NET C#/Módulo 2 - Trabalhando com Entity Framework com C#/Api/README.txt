-> Cria as migrações para serem aplicadas no banco de dados
dotnet-ef migrations add <nome-migrations>
    EX: dotnet-ef migrations add CriacaoTabelaContatos


-> Aplica as migrações no banco de dados
dotnet-ef database update
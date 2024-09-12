# 📡 MinimalAPI com .NET 8.0

Resolução do desafio da DIO. Construí a MinimalAPI usando .NET 8.0, Entity Framework, Tokens JWT e MySQL.


## ⚙ Configurando

É necessário ter o MySQL configurado com o usuário=root e senha=123456.

Para executar a API:
```shell
cd .\MinimalAPI\ 
cd .\API\

-> Verificando a versão do Entity Framework e instalando (Opcional)
dotnet ef --version
dotnet tool install --global dotnet-ef

-> Realizando as migrações
dotnet ef migrations add MigrationInicial
dotnet ef database update

-> Executando a API
dotnet run
```

Para executar os Testes:
```shell
cd .\MinimalAPI\ 
cd .\API.Tests\   

-> criando um database para testes
mysql -uroot -p'123456';
create database minimal_api_test;
exit;

-> Fazendo um dump da database
mysqldump -uroot -p'123456' minimal_api > minimal_api.dump.sql;
mysql -uroot -p'123456' minimal_api_test < minimal_api.dump.sql;
    
Se estiver no PowerShell então use este:
Get-Content minimal_api.dump.sql | mysql -uroot -p'123456' minimal_api_test

-> Testando
dotnet test
```
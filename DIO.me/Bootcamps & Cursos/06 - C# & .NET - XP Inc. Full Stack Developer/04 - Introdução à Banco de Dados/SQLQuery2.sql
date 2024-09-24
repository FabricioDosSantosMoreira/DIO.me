-- START TRAN
-- ROLLBACK


-- built-in functions
SELECT COUNT(*) QuantidadeProdutos FROM Produtos;

SELECT COUNT(*) QuantidadeProdutos FROM Produtos WHERE Tamanho = 'M';

SELECT SUM(Preco) PrecoTotal FROM Produtos;

SELECT SUM(Preco) PrecoTotal FROM Produtos WHERE Tamanho = 'M';

SELECT MAX(Preco) ProtudoMaisCaro FROM Produtos;

SELECT MAX(Preco) ProtudoMaisCaroTamanhoM FROM Produtos WHERE Tamanho = 'M';

SELECT MIN(Preco) ProtudoMaisBarato FROM Produtos;

SELECT MIN(Preco) ProtudoMaisBaratoTamanhoM FROM Produtos WHERE Tamanho = 'M';

SELECT AVG(Preco) FROM Produtos;



-- Concatenando Colunas
SELECT
	Nome + ' - ' + Cor AS NomeProduto
FROM Produtos

SELECT
	Nome + ' - ' + Cor AS NomeProdutoCompleto,
	Nome AS Nome,
	Cor AS Cor
FROM Produtos

SELECT
	Nome + ' - ' + Cor AS NomeProdutoCompleto,
	LOWER(Nome) AS Nome,
	LOWER(Cor) AS Cor
FROM Produtos

SELECT
	Nome + ' - ' + Cor AS NomeProdutoCompleto,
	UPPER(Nome) AS Nome,
	UPPER(Cor) AS Cor
FROM Produtos



-- Adicionando Colunas 
ALTER TABLE Produtos
ADD DataCadastro DATETIME2;

SELECT * FROM Produtos;

UPDATE Produtos
SET DataCadastro = GETDATE() WHERE Id >= 0;

-- Removendo Colunas
-- DROP COLUMN Produtos ADD DataCadastro DATETIME2;


SELECT
	Nome + ' - ' + Cor AS NomeProdutoCompleto,
	UPPER(Nome) AS Nome,
	LOWER(Cor) AS Cor,
	FORMAT(DataCadastro, 'dd/MM/yyyy - HH:mm') AS Data
FROM Produtos


-- Agrupando
SELECT 
	Tamanho, 
	COUNT(*) AS Quantidade
FROM Produtos
WHERE Tamanho <> '' 
GROUP BY Tamanho
ORDER BY Quantidade DESC;

SELECT * FROM Clientes;


-- Ajuste para adicionar chave primária corretamente
ALTER TABLE Clientes
ADD CONSTRAINT PK_Clientes PRIMARY KEY(Id);

-- Criação da tabela Enderecos com chave estrangeira
CREATE TABLE Enderecos (
    Id int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    IdCliente int NULL,
    Rua varchar(255) NULL,
    Bairro varchar(255) NULL,
    Cidade varchar(255) NULL,
    Estado varchar(255) NULL,

    CONSTRAINT FK_Enderecos_Clientes FOREIGN KEY(IdCliente)
    REFERENCES Clientes(Id)
);


SELECT * FROM Clientes;
SELECT * FROM Enderecos;

INSERT INTO Enderecos VALUES (4, 'Rua X', 'Bairro Y', 'Cidade Z', 'Estado A');

SELECT * FROM Clientes WHERE Id = 4;
SELECT * FROM Enderecos WHERE IdCliente = 4;


-- Joins 
SELECT * FROM Clientes 
INNER JOIN Enderecos ON Clientes.Id = Enderecos.IdCliente
WHERE Clientes.Id = 4;


SELECT 
	Clientes.Nome + ' ' + Clientes.Sobrenome AS NomeCompleto, 
	Enderecos.Cidade + ' ' + Enderecos.Rua + ' ' + Enderecos.Bairro as Endereco
FROM Clientes 
	INNER JOIN Enderecos ON Clientes.Id = Enderecos.IdCliente
WHERE Clientes.Id = 4;


SELECT 
	C.Nome + ' ' + C.Sobrenome AS NomeCompleto, 
	E.Cidade + ' ' + E.Rua + ' ' + E.Bairro as Endereco
FROM Clientes C
	INNER JOIN Enderecos E ON C.Id = E.IdCliente
WHERE C.Id = 4;



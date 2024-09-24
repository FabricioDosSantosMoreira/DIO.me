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



CREATE TABLE Clientes (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nome NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    DataNascimento DATETIME2,
    Telefone NVARCHAR(15),
    Endereco NVARCHAR(255)
);


INSERT INTO Clientes (Nome, Email, DataNascimento, Telefone, Endereco) 
VALUES 
('João Silva', 'joao.silva@email.com', '1985-05-10', '(11) 98765-4321', 'Rua das Flores, 123'),
('Maria Souza', 'maria.souza@email.com', '1990-12-22', '(21) 99876-5432', 'Av. Paulista, 456'),
('Pedro Santos', 'pedro.santos@email.com', '1978-03-14', '(31) 91234-5678', 'Rua dos Bobos, 0');

SELECT * FROM Clientes;

BEGIN TRAN
ROLLBACK

DELETE Clientes WHERE Id = 1;

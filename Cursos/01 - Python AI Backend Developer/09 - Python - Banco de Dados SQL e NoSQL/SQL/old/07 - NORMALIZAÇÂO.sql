SELECT * FROM viagens.usuarios


# me apaga dps
DELETE FROM viagens.usuarios WHERE id = 4;


# Normalização de dados

ALTER TABLE viagens.usuarios
ADD COLUMN rua VARCHAR(100),
ADD COLUMN numero VARCHAR(10),
ADD COLUMN cidade VARCHAR(50),
ADD COLUMN estado VARCHAR(20);

SELECT * FROM viagens.usuarios

-- Copia os dados da tabela original para a nova tabela
UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
    cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
    estado = SUBSTRING_INDEX(endereco, ',', -1);
    
ALTER TABLE viagens.usuarios
DROP COLUMN endereco; 

SELECT * FROM viagens.usuarios;

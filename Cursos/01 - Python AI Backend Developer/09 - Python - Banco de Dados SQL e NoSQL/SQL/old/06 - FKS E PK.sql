# - - - - -> PRIMARY KEYS:

# 		As chaves primárias (primary keys) são colunas em uma tabela que garantem a unicidade e 
# a identificação exclusiva de cada registro na tabela. Cada tabela pode ter no máximo uma 
# chave primária e nenhum valor nulo é permitido em uma chave primária.



# - - -> Sintaxe: 

# CREATE TABLE ***Criando uma tabela com PK
#		{{tabela}}
# (id INT PRIMARY KEY AUTOINCREMENT,
# … );


# ALTER TABLE 
#		{{tabela}}
# MODIFY COLUMN 
#		id INT PRIMARY KEY;



# - - - >Exemplos:

# Modifica a coluna 'id' na tabela 'usuarios' para uma chave primaária.
ALTER TABLE viagens.usuarios
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

# Modifica a coluna 'id' na tabela 'destinos' para uma chave primaária.
ALTER TABLE viagens.destinos
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

# Modifica a coluna 'id' na tabela 'reservas' para uma chave primaária.
ALTER TABLE viagens.reservas
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

SELECT * FROM viagens.reservas



# - - - - -> FOREIGN KEYS:

# 		As chaves estrangeiras (foreign keys) são colunas em uma tabela que estabelecem 
# uma relação entre essa tabela e uma tabela referenciada. Essa relação é baseada em 
# valores correspondentes entre as colunas das duas tabelas. A chave estrangeira em 
# uma tabela é geralmente uma referência à chave primária de outra tabela.

# - - -> Sintaxe: 

# CREATE TABLE 
#		{{tabela}} 
#			(id INT PRIMARY KEY,
#			chave_estrangeira INT,
#	FOREIGN KEY (chave_estrangeira) REFERENCES {{outra_tabela}} (id)
# );


# ALTER TABLE
#	 	{{tabela}}
# ADD CONSTRAINT 
#		{{nome_constraint}}
# FOREIGN KEY (id_outra_tabela)
# REFERENCES {{outra_tabela}} (id)



# - - - >Exemplos:

ALTER TABLE viagens.reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES viagens.usuarios (id);


ALTER TABLE viagens.reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino) REFERENCES viagens.destinos (id);

SELECT * FROM viagens.reservas;

# isso vai dar erro pois referencia a ids que nao excistem
INSERT INTO viagens.reservas (id_usuario, id_destino, data)
VALUES (6, 6, '2024-11-11');

# isso vai dar certo pois referencia um id que existe
INSERT INTO viagens.reservas (id_usuario, id_destino, data)
VALUES (1, 1, '2024-10-09');





ALTER TABLE viagens.reservas DROP CONSTRAINT fk_reservas_usuarios;
ALTER TABLE viagens.reservas 
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES viagens.usuarios (id)
ON DELETE CASCADE;


SELECT * FROM viagens.usuarios;
SELECT * FROM viagens.reservas;

DELETE FROM viagens.usuarios
WHERE id = 1;


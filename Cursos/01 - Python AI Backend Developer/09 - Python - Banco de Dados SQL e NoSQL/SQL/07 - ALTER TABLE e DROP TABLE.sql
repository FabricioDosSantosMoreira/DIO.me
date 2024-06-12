# - - - - -> ALTER TABLE:

# - - -> Sintaxe:

# ALTER TABLE 
#		{{nome_da_tabela}}
#		{{ação}};



# - - -> Ações:

#				As ações são fundamentais para modificar a estrutura das tabelas em SQL. Entre elas:

#					- ADD COLUMN (Adicionar coluna): adiciona uma nova coluna à tabela.
# 					- DROP COLUMN (Remover coluna): remove uma coluna existente da tabela.
# 					- MODIFY COLUMN (Modificar tipo de dados): modifica a definição de uma coluna existente.
# 					- RENAME COLUMN (Renomear coluna): renomeia uma coluna existente.
# 					- ADD CONSTRAINT (Adicionar restrição): adiciona uma nova restrição à tabela.
# 					- DROP CONSTRAINT (Remover restrição): remove uma restrição existente da tabela.
#					- RENAME TO (Renomear tabela): renomeia a tabela.



# - - - - -> DROP TABLE:

# - - -> Sintaxe:

# DROP TABLE 
#		{{tabela}}



# - - -> Problema: 

#				Usuários com endereços longos não estão conseguindo realizar cadastro no sistema
	
	
	
# - - -> Solução 1: Recriar a tabela, migrar os dados e excluir a tabela anterior

# Cria uma nova tabela com as mudanças necessárias na coluna 'endereço'.
CREATE TABLE viagens.usuarios_temp (
   id INT COMMENT 'Identificador único do usuário',
   nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
   email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário',
   data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
   endereco VARCHAR(150) NOT NULL COMMENT 'Endereço do usuário'
);

# Insere na nova tabela os dados da tabela antiga.
INSERT INTO viagens.usuarios_temp (id, nome, email, data_nascimento, endereco)
SELECT id, nome, email, data_nascimento, endereco 
FROM viagens.usuarios;

# Seleciona tudo da nova tabela.
SELECT * FROM viagens.usuarios_temp;

# Exclui permanentemente a tabela 'usuarios'.
DROP TABLE viagens.usuarios;

# Renomeia a nova tabela para 'usuarios'.
ALTER TABLE viagens.usuarios_temp RENAME usuarios

# Seleciona tudo da nova tabela.
SELECT * FROM viagens.usuarios;



# - - -> Solução 2: Alterar estrutura da tabela

# Altera o tamanho da coluna  'endereco' na tabela 'usuarios'.
ALTER TABLE viagens.usuarios MODIFY COLUMN endereco VARCHAR(200);

# Seleciona tudo da tabela.
SELECT * FROM viagens.usuarios;

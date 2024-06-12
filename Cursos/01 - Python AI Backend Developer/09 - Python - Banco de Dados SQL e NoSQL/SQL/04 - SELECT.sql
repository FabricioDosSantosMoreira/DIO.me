# - - - - -> SELECT: 

# - - -> Sintaxe:

# SELECT {{lista_colunas}} ***Onde '*' retorna todas as colunas
# FROM tabela;
# WHERE {{condição}} ***Nem sempre uma condição é necessária



# - - -> Operadores:

# 				Os operadores são fundamentais para criar condições em consultas SQL, permitindo
#			filtrar dados com base em critérios específicos. Entre eles:
#
# 				- = (Igual a): comparação de igualdade.
# 				- <> (Diferente de): comparação de desigualdade.
# 				- > (Maior que): comparação de magnitude.
# 				- < (Menor que): comparação de magnitude.
# 				- >= (Maior ou igual a): comparação de magnitude.
# 				- <= (Menor ou igual a): todos os critérios devem ser verdadeiros.
#				- AND (Operador lógico E): todos os critérios devem ser verdadeiros.
# 				- OR (Operador lógico OU): pelo menos um critério deve ser verdadeiro.
# 				- NOT (Operador lógico NÃO): inverte o valor do critério.
# 				- BETWEEN (Dentro de um intervalo): Verifica se um valor está dentro de um intervalo especificado.
# 				- IN (Pertence a uma lista de valores): Verifica se um valor está presente em um conjunto de valores.
# 				- LIKE (Comparação de padrões): Realiza correspondência parcial em strings usando caracteres curinga (% para múltiplos caracteres, _ para um único caractere).
# 				- IS NULL (O valor é nulo): Verifica se um valor é nulo.
# 				- IS NOT NULL (O valor não é nulo): Verifica se um valor não é nulo.



# - - -> Exemplos:

# Seleciona todas as colunas da tabela 'usuarios'.
SELECT * FROM viagens.usuarios;

# Seleciona todas as colunas da tabela 'destinos'.
SELECT * FROM viagens.destinos;

# Seleciona todas as colunas da tabela 'reservas'.
SELECT * FROM viagens.reservas;


# Seleciona apenas o 'nome' e o 'email' da tabela 'usuarios'.
SELECT nome, email FROM viagens.usuarios;


# Seleciona tadas as colunas da tabela 'usuarios' onde 'nome' é "João Silva".
SELECT * FROM viagens.usuarios WHERE nome = 'João Silva';


# Seleciona todas as colunas da tabela 'usuarios' onde 'id' é igual a 1 e 
# 'nome' possui os caracteres Teste.
SELECT * FROM viagens.usuarios
WHERE id = 1 AND nome LIKE '%Teste%';


# Seleciona todas as colunas da tabela 'usuarios' onde 'id' é igual a 1 ou 
# 'nome' possui os caracteres Mariana.
SELECT * FROM viagens.usuarios 
WHERE id = 1 OR nome LIKE '%Mariana%';


# Seleciona todas as colunas da tabela 'usuarios' onde
# a 'data_nascimento' é menor que '1990-01-01'.
SELECT * FROM viagens.usuarios WHERE data_nascimento < '1990-01-01';


# Seleciona todas as colunas da tabela 'usuarios' onde
# a 'nome' possui o padrão 'Oliveira'.
SELECT * FROM viagens.usuarios WHERE nome LIKE '%Oliveira%';


# Seleciona todas as colunas da tabela 'usuarios' onde
# a 'nome' possui o padrão 'M_ria__'.
SELECT * FROM viagens.usuarios WHERE nome LIKE '%M_ria__%';


# Seleciona todas as reservas pendentes, juntamente com o nome do usuário e o destino da viagem.
SELECT r.id, u.nome AS usuario, d.nome AS destino, r.data
FROM viagens.reservas r
JOIN viagens.usuarios u ON r.id_usuario = u.id
JOIN viagens.destinos d ON r.id_destino = d.id
WHERE r.status = 'pendente';


# Seleciona as reservas feitas por um usuário específico, incluindo informações sobre o destino, data e status.
SELECT r.id, d.nome AS destino, r.data, r.status
FROM viagens.reservas r
JOIN viagens.destinos d ON r.id_destino = d.id
WHERE r.id_usuario = (SELECT id FROM viagens.usuarios WHERE nome = 'Mariana Ferreira');


# Seleciona o número total de reservas para cada destino e os retorna juntamente com o nome do destino 
# e 'total_reservas' em ordem descendente.
SELECT d.nome AS destino, COUNT(*) AS total_reservas
FROM viagens.reservas r
JOIN viagens.destinos d ON r.id_destino = d.id
GROUP BY d.nome 
ORDER BY total_reservas DESC;


# Seleciona as reservas feitas por um usuário que possua a letra 'a' no nome.
SELECT r.id, u.nome AS usuario, d.nome AS destino, r.data, r.status
FROM viagens.reservas r
JOIN viagens.usuarios u ON r.id_usuario = u.id
JOIN viagens.destinos d ON r.id_destino = d.id
WHERE u.nome LIKE '%a%';
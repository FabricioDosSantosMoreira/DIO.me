# - - - - -> UPDATE:

# - - -> Sintaxe:

# UPDATE {{tabela}}
# SET
# 		{{coluna_1}} = {{novo_valor_1}},
# 		{{coluna_2}} = {{novo_valor_2}}
# WHERE
# 		{{condição}} ;



# - - -> Exemplos: 

# Atualiza o 'id' do usuario que tem o 'email' igual a 'teste@gmail.com'.
UPDATE viagens.usuarios
SET id = 11000
WHERE email = 'teste@gmail.com';

# Seleciona o usuario com o 'id' igual a 11000.
SELECT * FROM viagens.usuarios
WHERE id = 11000;


# Atualiza o 'id' do usuario que tem o 'email' igual a 'teste@gmail.com'.
UPDATE viagens.usuarios
SET id = 1
WHERE email = 'teste@gmail.com';

# Seleciona o usuario com o 'id' igual a 1.
SELECT * FROM viagens.usuarios
WHERE id = 1;

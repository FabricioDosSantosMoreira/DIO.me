# - - - - -> DELETE:

# - - -> Sintaxe:
 
# DELETE FROM   		***OBS NUNCA fazer DELETE sem WHERE
# 		{{tabela}}
# WHERE 					
# 		{{condição}};



# - - -> Exemplos: 

# Seleciona o destino com o nome igual a 'Destino teste'.
SELECT * FROM viagens.destinos
WHERE nome = 'Destino teste';


# Deleta  o destino onde o nome é Destino teste'.
DELETE FROM viagens.destinos
WHERE nome = 'Destino teste';


# Seleciona o destino com o nome igual a 'Destino teste'.
SELECT * FROM viagens.destinos
WHERE nome = 'Destino teste';

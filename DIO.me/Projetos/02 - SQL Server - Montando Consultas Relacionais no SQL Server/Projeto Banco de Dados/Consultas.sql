-- 1. Buscar o nome e ano dos filmes
SELECT Nome, Ano FROM Filmes;


-- 2. Buscar o nome, ano e duração dos filmes, ordenados por ordem crescente pelo ano
SELECT Nome, Ano, Duracao FROM Filmes ORDER BY Ano ASC;


-- 3. Buscar pelo filme de volta para o futuro, trazendo o nome, ano e a duração
SELECT Nome, Ano, Duracao FROM Filmes WHERE LOWER(Nome) LIKE 'de volta para o futuro';
SELECT Nome, Ano, Duracao FROM Filmes WHERE LOWER(Nome) = 'de volta para o futuro';


-- 4. Buscar os filmes lançados em 1997
SELECT F.Nome, F.Ano, F.Duracao FROM Filmes F WHERE F.Ano = 1997;


-- 5. Buscar os filmes lançados APÓS o ano 2000
 SELECT F.Nome, F.Ano, F.Duracao FROM Filmes F WHERE F.Ano >= 2000;


-- 6. Buscar os filmes com a duracao maior que 100 e menor que 150, ordenando pela duracao em ordem crescente
 SELECT 
	F.Nome, F.Ano, F.Duracao 
FROM 
	Filmes F 
WHERE 
	F.Duracao > 100 AND F.Duracao < 150 
ORDER BY 
	F.Duracao ASC;


-- 7. Buscar a quantidade de filmes lançadas no ano, agrupando por ano, ordenando pela quantidade em ordem decrescente
SELECT 
    F.Ano, 
    COUNT(*) AS Quantidade 
FROM 
    Filmes F 
GROUP BY 
    F.Ano
ORDER BY
	Quantidade DESC;


-- 8. Buscar os Atores do gênero masculino, retornando o PrimeiroNome, UltimoNome
SELECT A.PrimeiroNome, A.UltimoNome FROM Atores A WHERE A.Genero = 'M';


-- 9. Buscar os Atores do gênero feminino, retornando o PrimeiroNome, UltimoNome, e ordenando pelo PrimeiroNome
SELECT 
	A.PrimeiroNome, A.UltimoNome 
FROM 
	Atores A 
WHERE 
	A.Genero = 'F'
ORDER BY
	A.PrimeiroNome;


-- 10. Buscar o nome do filme e o gênero
SELECT 
	F.Nome AS Filme, G.Genero AS Gênero
FROM Filmes F 
	JOIN FilmesGenero FG ON F.Id = FG.IdFilme
	JOIN Generos G ON G.Id = FG.IdGenero;


-- 11. Buscar o nome do filme e o gênero do tipo "Mistério"
SELECT 
	F.Nome AS Filme, G.Genero AS Gênero
FROM Filmes F 
	JOIN FilmesGenero FG ON F.Id = FG.IdFilme
	JOIN Generos G ON G.Id = FG.IdGenero
WHERE
	G.Genero = 'Mistério';


-- 12. Buscar o nome do filme e os atores, trazendo o PrimeiroNome, UltimoNome e seu Papel
SELECT 
	F.Nome AS Filme, A.PrimeiroNome, A.UltimoNome, EF.Papel
FROM Filmes F 
	JOIN ElencoFilme EF ON F.Id = EF.IdFilme
	JOIN Atores A ON A.Id = EF.IdAtor;

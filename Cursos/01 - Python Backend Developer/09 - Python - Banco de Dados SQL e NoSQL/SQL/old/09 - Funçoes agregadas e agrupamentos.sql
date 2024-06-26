


SELECT COUNT(*) AS total_usuarios FROM viagens.usuarios





SELECT COUNT(*) AS total_usuarios_com_reservas FROM viagens.usuarios AS u
INNER JOIN reservas AS r ON u.id = r.id_usuario

-- Media da idade dos usuarios
SELECT AVG(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS idade
FROM usuarios;

-- Soma da idade dos usuarios
SELECT SUM(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade
FROM usuarios


SELECT MIN(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS maior_idade
FROM usuarios



INSERT INTO reservas (id_usuario, id_destino) VALUES (2, 3)


SELECT COUNT(*) AS qtd_reservas, id_destino FROM reservas
GROUP BY id_destino



SELECT COUNT(*) AS qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas DESC

SELECT COUNT(*) AS qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas ASC, id_destino ASC



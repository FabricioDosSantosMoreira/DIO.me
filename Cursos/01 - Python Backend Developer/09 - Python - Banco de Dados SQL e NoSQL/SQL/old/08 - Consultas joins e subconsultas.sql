SELECT * FROM viagens.usuarios AS us
INNER JOIN viagens.reservas AS rs ON us.id = rs.id_usuario
INNER JOIN viagens.destinos AS ds ON ds.id = rs.id_destino;




INSERT INTO viagens.usuarios (nome, email, data_nascimento, rua , numero, cidade, estado)
VALUES ('sem_reservas', 'sem_reservas@gmail.com', '1980-01-01', 'rua', '12', 'cidade', 'estado');

SELECT * FROM viagens.usuarios AS us
INNER JOIN reservas AS rs ON us.id = rs.id_usuario;

SELECT * FROM viagens.usuarios AS us
LEFT JOIN reservas AS rs ON us.id = rs.id_usuario;





INSERT INTO viagens.destinos (nome, descricao)
VALUES ('destino sem reservas', 'descricao')

SELECT * FROM viagens.reservas AS rs
RIGHT JOIN destinos AS ds ON rs.id_destino = ds.id;




# Sub consultas ou consultas aninhadas
SELECT * FROM viagens.destinos
WHERE id NOT IN (SELECT id_destino FROM reservas)



SELECT * FROM viagens.usuarios
WHERE id NOT IN (SELECT id_usuario FROM reservas)



SELECT nome, (SELECT COUNT(*) FROM reservas WHERE id_usuario = usuarios.id) AS total_reservas
FROM usuarios;



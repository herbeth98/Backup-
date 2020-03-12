--CRIAR UM BANCO DE DADOS
CREATE DATABASE info_mod2_atividades;

--MOSTRAR OS BANCOS DE DADOS
SHOW DATABASES;

--UTILIZAR O BANCO DE DADOS
USE info_mod2_atividades;


--CRIAR UMA TABELA E SUAS COLUNAS, O VARCHAR SIGNIFICA a quantidade de Caracteres da categoria
CREATE TABLE jogador_de_futebol
(
nome VARCHAR(80),
id INTEGER(7),
data_nasc DATE,
nacionalidade VARCHAR(20),
clube VARCHAR(20),
PRIMARY KEY (id)
);

--Visualizar o conteúdo cadastado em uma Tabela!
SELECT * FROM jogador_de_futebol;

--INSERIR NA TABELA COM AS COLUNAS NA MESMA ORDEM QUE SEUS VALORES
INSERT INTO jogador_de_futebol
(nome, id, data_nasc, nacionalidade, clube)
VALUES
('Marc André Ter Stegen',01,'1992-04-30','Belgico','Barcelona'),
('Neto',02,'1989-07-19','Brasileiro','Barcelona'),
('Clément Lenglet',03,'1995-06-17','Frances','Barcelona'),
('Samuel Umtiti',04,'1992-04-30','Alemão','Barcelona'),
('Marc-André ter Stegen',05,'1993-11-04','Frances','Barcelona');
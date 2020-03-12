--CRIAR UM BANCO DE DADOS
CREATE DATABASE banco01;

--MOSTRAR OS BANCOS DE DADOS
SHOW DATABASES;

--UTILIZAR O BANCO DE DADOS
USE banco01;

--Visualizar o conteúdo cadastado em uma Tabela!
SELECT * FROM cadastro_aluno;

--CRIAR UMA TABELA E SUAS COLUNAS, O VARCHAR SIGNIFICA a quantidade de Caracteres da categoria
CREATE TABLE cadastro_aluno
(
nome VARCHAR(80),
sexo VARCHAR(1),
matricula INTEGER(7),
email VARCHAR(80),
data_nasc DATE,
estado_civil VARCHAR(20),
cidade VARCHAR (25),
uf VARCHAR(2),
PRIMARY KEY (matricula)
);

--INSERIR NA TABELA COM AS COLUNAS NA MESMA ORDEM QUE SEUS VALORES
INSERT INTO cadastro_aluno
(nome,sexo,matricula,email,data_nasc,estado_civil,cidade,uf)
VALUES
('Herbeth Sousa','M',090102,"portaldj.12@gmail.com",'2002-01-19','Solteiro','Afrânio','PE'),
("Carlos Teves","M",129900,"cacateves@hotmail.com","1987-09-09","Casado","Paulistana","PI"),
("Astrogilda Smith","F",779900,"astrogirl@gmail.com","1983-10-03","Solteira","Picos","PI"),
("Sávio Gonzaga","M",131,"savin@gmail.com","1963-11-19","Solteiro","Petrolina","PE"),
("João das Neves","M",2290,"jsnow@hotmail.com","1929-09-09","Casado","Campinas","SP"),
("Janete Tancredo","F",2299,"janetefire@hotmail.com","1931-09-09","Casada","Campinas","SP");



INSERT INTO cadastro_aluno
(nome,sexo,matricula,data_nasc,estado_civil,cidade,uf)
VALUES
("Francisco Zidane","M",8091,"1993-03-08","Solteiro","Paulistana","PI");
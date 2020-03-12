--CRIAR UM BANCO DE DADOS
CREATE DATABASE info_mod2_atividades;

--MOSTRAR OS BANCOS DE DADOS
SHOW DATABASES;

--UTILIZAR O BANCO DE DADOS
USE info_mod2_atividades;


--CRIAR UMA TABELA E SUAS COLUNAS, O VARCHAR SIGNIFICA a quantidade de Caracteres da categoria
CREATE TABLE filme
(
nome VARCHAR(80),
id INTEGER(7),
data_lanc DATE,
sinopse TEXT,
PRIMARY KEY (id)
);

--Visualizar o conteúdo cadastado em uma Tabela!
SELECT * FROM filme;

--INSERIR NA TABELA COM AS COLUNAS NA MESMA ORDEM QUE SEUS VALORES
INSERT INTO filme
(nome, id, data_lanc,sinopse)
VALUES
('Vingadores: Ultimato',01,"2019-04-25","Após Thanos eliminar metade das criaturas vivas, os Vingadores têm de lidar com a perda de amigos e entes queridos. Com Tony Stark vagando perdido no espaço sem água e comida, Steve Rogers e Natasha Romanov lideram a resistência contra o titã louco."),
("Esquadrão Suicida",02,"2016-08-04","Um time dos mais perigosos e encarcerados supervilões são contratados por uma agência secreta do governo, para combater uma poderosa entidade. No entanto, quando eles percebem que não foram escolhidos apenas para ter sucesso, mas também por sua óbvia culpa quando inevitavelmente falharem, terão que decidir se vale a pena ou não continuar correndo risco de morte."),
("Coringa",03,"2019-10-3","Isolado, intimidado e desconsiderado pela sociedade, o fracassado comediante Arthur Fleck inicia seu caminho como uma mente criminosa após assassinar três homens em pleno metrô. Sua ação inicia um movimento popular contra a elite de Gotham City, da qual Thomas Wayne é seu maior representante."),
("O Poderoso Chefão",04,"1972-03-24","Don Vito Corleone (Marlon Brando) é o chefe de uma família de Nova York que está feliz, pois Connie (Talia Shire), sua filha, se casou com Carlo... "),
(" A Lista de Schindler",05,"2019-05-01","A inusitada história de Oskar Schindler (Liam Neeson), um sujeito oportunista, sedutor, armador, simpático, comerciante no mercado negro, mas,... "),
(" Um Sonho de Liberdade ",06,"1995-05-06","Em 1946, Andy Dufresne (Tim Robbins), um jovem e bem sucedido banqueiro, tem a sua vida radicalmente modificada ao ser condenado por um crime que... "),
("O Rei Leão ",07,"2011-05-06","Mufasa (voz de James Earl Jones), o Rei Leão, e a rainha Sarabi (voz de Madge Sinclair) apresentam ao reino o herdeiro do trono, Simba (voz de.."),
(" O Senhor dos Anéis - O Retorno do Rei",08,"2003-08-05","Sauron planeja um grande ataque a Minas Tirith, capital de Gondor, o que faz com que Gandalf (Ian McKellen) e Pippin (Billy Boyd) partam para o... "),
(" Forrest Gump - O Contador de Histórias ",09,"1994-12-07","Quarenta anos da história dos Estados Unidos, vistos pelos olhos de Forrest Gump (Tom Hanks), um rapaz com QI abaixo da média e boas intenções. Por... "),
(" À Espera de um Milagre ", 10, "2000-03-10","1935, no corredor da morte de uma prisão sulista. Paul Edgecomb (Tom Hanks) é o chefe de guarda da prisão, que temJohn Coffey (Michael Clarke... ");

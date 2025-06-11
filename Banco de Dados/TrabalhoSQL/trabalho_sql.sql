-- Equipe: Saul Alves, Guilherme Chaves e Paulo Henrique

create schema registro_multas;

use registro_multas;

CREATE TABLE Infrator (
    id_infrator INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(200),
    numero_cnh VARCHAR(15) UNIQUE,
    data_nascimento DATE
);

CREATE TABLE Infracao (
    id_infracao INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(200),
    pontuacao INT,
    valor_multa DECIMAL(10, 2)
);

CREATE TABLE Multa (
    id_multa INT AUTO_INCREMENT PRIMARY KEY,
    data_multa DATE,
    id_infrator INT,
    id_infracao INT,
    status_pagamento ENUM('pago', 'pendente'),
    FOREIGN KEY (id_infrator) REFERENCES Infrator(id_infrator),
    FOREIGN KEY (id_infracao) REFERENCES Infracao(id_infracao)
);



INSERT INTO Infrator (nome, endereco, numero_cnh, data_nascimento)
VALUES ('João Silva', 'Rua A, 123', '12345678901', '1985-06-15');

INSERT INTO Infrator (nome, endereco, numero_cnh, data_nascimento)
VALUES ('Maria Oliveira', 'Rua B, 456', '98765432100', '1990-08-22');

INSERT INTO Infrator (nome, endereco, numero_cnh, data_nascimento)
VALUES ('Carlos Souza', 'Rua C, 789', '11223344556', '1982-03-05');

INSERT INTO Infrator (nome, endereco, numero_cnh, data_nascimento)
VALUES ('Ana Martins', 'Rua D, 101', '66778899001', '1995-11-30');


-- Inserir infrações
INSERT INTO Infracao (descricao, pontuacao, valor_multa)
VALUES ('Excesso de Velocidade', 7, 150.00);

INSERT INTO Infracao (descricao, pontuacao, valor_multa)
VALUES ('Estacionamento Irregular', 3, 50.00);

INSERT INTO Infracao (descricao, pontuacao, valor_multa)
VALUES ('Ultrapassagem Proibida', 5, 200.00);

INSERT INTO Infracao (descricao, pontuacao, valor_multa)
VALUES ('Uso de Celular ao Volante', 4, 80.00);


-- Inserir multas
INSERT INTO Multa (data_multa, id_infrator, id_infracao, status_pagamento)
VALUES ('2024-10-01', 1, 1, 'pendente');

INSERT INTO Multa (data_multa, id_infrator, id_infracao, status_pagamento)
VALUES ('2024-09-25', 2, 2, 'pago');

INSERT INTO Multa (data_multa, id_infrator, id_infracao, status_pagamento)
VALUES ('2024-10-02', 3, 3, 'pendente');

INSERT INTO Multa (data_multa, id_infrator, id_infracao, status_pagamento)
VALUES ('2024-10-03', 4, 4, 'pago');

INSERT INTO Multa (data_multa, id_infrator, id_infracao, status_pagamento)
VALUES ('2024-10-05', 1, 2, 'pendente');


INSERT INTO Multa (data_multa, id_infrator, id_infracao, status_pagamento)
VALUES ('2024-10-05', 2, 1, 'pago');



-- Consultas:

-- Listar todas as infrações com suas pontuações e valores de multa:

SELECT id_infracao, descricao, pontuacao, valor_multa
FROM Infracao;

-- Listar todos os infratores e suas respectivas CNHs:

SELECT id_infrator, nome, numero_cnh
FROM Infrator;

-- Listar infratores com multas pendentes acima de um valor específico
-- (por exemplo, R$100):

SELECT I.nome, Inf.descricao, Inf.valor_multa, M.data_multa
FROM Multa M
JOIN Infrator I ON M.id_infrator = I.id_infrator
JOIN Infracao Inf ON M.id_infracao = Inf.id_infracao
WHERE M.status_pagamento = 'pendente' AND Inf.valor_multa > 100
limit 0, 1000;

-- Consultar o total de multas (em valor) de cada infrator:

SELECT I.nome, SUM(Inf.valor_multa) AS total_multa
FROM Multa M
JOIN Infrator I ON M.id_infrator = I.id_infrator
JOIN Infracao Inf ON M.id_infracao = Inf.id_infracao
GROUP BY I.nome;

-- Listar infratores que têm mais de uma multa:

SELECT I.nome, COUNT(M.id_multa) AS quantidade_multas
FROM Multa M
JOIN Infrator I ON M.id_infrator = I.id_infrator
GROUP BY I.nome
HAVING COUNT(M.id_multa) > 1;

-- Buscar multas que foram pagas no último mês:

SELECT I.nome, Inf.descricao, M.data_multa
FROM Multa M
JOIN Infrator I ON M.id_infrator = I.id_infrator
JOIN Infracao Inf ON M.id_infracao = Inf.id_infracao
WHERE M.status_pagamento = 'pago' AND M.data_multa BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AND CURDATE();










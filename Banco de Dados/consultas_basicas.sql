-- 1) Tipos de dados permitidos para atributos em SQL:
-- SQL suporta uma variedade de tipos de dados, incluindo:
-- Numéricos: INT, SMALLINT, DECIMAL, FLOAT, DOUBLE PRECISION
-- Caracteres: CHAR, VARCHAR, TEXT
-- Datas e horas: DATE, TIME, TIMESTAMP, INTERVAL
-- Booleanos: BOOLEAN
-- Outros: BLOB, UUID

-- 2) Implementação de restrições de integridade:
-- Integridade de entidade: Garantida com PRIMARY KEY
CREATE TABLE DEPARTAMENTO (
    dnumero INT PRIMARY KEY,
    dnome VARCHAR(15) NOT NULL
);

-- Integridade referencial: Garantida com FOREIGN KEY
CREATE TABLE FUNCIONARIO (
    cpf CHAR(11) PRIMARY KEY,
    dnr INT,
    CONSTRAINT FK_DNR FOREIGN KEY (dnr) REFERENCES DEPARTAMENTO (dnumero)
);

-- 3) Comandos para consultas:
-- SELECT: Extrai dados de uma tabela
SELECT pnome, unome FROM FUNCIONARIO;

-- WHERE: Filtra linhas com base em uma condição
SELECT * FROM FUNCIONARIO WHERE salario > 3000;

-- JOIN: Combina linhas de tabelas diferentes
SELECT f.pnome, d.dnome 
FROM FUNCIONARIO f
JOIN DEPARTAMENTO d ON f.dnr = d.dnumero;

-- GROUP BY: Agrupa linhas que têm valores em comum
SELECT dnr, COUNT(*) 
FROM FUNCIONARIO 
GROUP BY dnr;

-- ORDER BY: Ordena os resultados de uma consulta
SELECT pnome FROM FUNCIONARIO ORDER BY pnome ASC;

-- HAVING: Filtra grupos de resultados (usado com GROUP BY)
SELECT dnr, AVG(salario) 
FROM FUNCIONARIO 
GROUP BY dnr 
HAVING AVG(salario) > 3000;

-- 4) Criação do banco de dados EMPRESA
CREATE SCHEMA EMPRESA;

-- Criação das tabelas do banco de dados EMPRESA
CREATE TABLE EMPRESA.FUNCIONARIO (
    cpf CHAR(11) PRIMARY KEY,
    pnome VARCHAR(15) NOT NULL,
    minicial CHAR,
    unome VARCHAR(15) NOT NULL,
    datanasc DATE,
    endereco VARCHAR(50),
    sexo CHAR,
    salario DECIMAL(10, 2),
    cpf_supervisor CHAR(11),
    dnr INT,
    FOREIGN KEY (cpf_supervisor) REFERENCES EMPRESA.FUNCIONARIO(cpf),
    FOREIGN KEY (dnr) REFERENCES EMPRESA.DEPARTAMENTO(dnumero)
);

CREATE TABLE EMPRESA.DEPARTAMENTO (
    dnumero INT PRIMARY KEY,
    dnome VARCHAR(15) NOT NULL,
    cpf_gerente CHAR(11) NOT NULL,
    data_inicio_gerente DATE,
    FOREIGN KEY (cpf_gerente) REFERENCES EMPRESA.FUNCIONARIO(cpf)
);

CREATE TABLE EMPRESA.PROJETO (
    projnumero INT PRIMARY KEY,
    projnome VARCHAR(15) NOT NULL,
    projlocal VARCHAR(15),
    dnum INT,
    FOREIGN KEY (dnum) REFERENCES EMPRESA.DEPARTAMENTO(dnumero)
);

CREATE TABLE EMPRESA.TRABALHA_EM (
    fcpf CHAR(11),
    pnr INT,
    horas DECIMAL(3,1),
    PRIMARY KEY (fcpf, pnr),
    FOREIGN KEY (fcpf) REFERENCES EMPRESA.FUNCIONARIO(cpf),
    FOREIGN KEY (pnr) REFERENCES EMPRESA.PROJETO(projnumero)
);

CREATE TABLE EMPRESA.DEPENDENTE (
    fcpf CHAR(11),
    nome_dependente VARCHAR(15),
    sexo CHAR,
    datanasc DATE,
    parentesco VARCHAR(8),
    PRIMARY KEY (fcpf, nome_dependente),
    FOREIGN KEY (fcpf) REFERENCES EMPRESA.FUNCIONARIO(cpf)
);

-- 5) Consultas no esquema EMPRESA:
-- a) Funcionários do departamento 5 que trabalham mais de 10 horas no projeto ProdutoX
SELECT f.pnome, f.unome
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.TRABALHA_EM te ON f.cpf = te.fcpf
JOIN EMPRESA.PROJETO p ON te.pnr = p.projnumero
WHERE f.dnr = 5 AND te.horas > 10 AND p.projnome = 'ProdutoX';

-- b) Funcionários com o mesmo nome de um dependente
SELECT f.pnome
FROM EMPRESA.FUNCIONARIO f
WHERE EXISTS (
    SELECT 1
    FROM EMPRESA.DEPENDENTE d
    WHERE f.pnome = d.nome_dependente
);

-- c) Funcionários supervisionados por Fernando Wong
SELECT f.pnome, f.unome
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.FUNCIONARIO sup ON f.cpf_supervisor = sup.cpf
WHERE sup.pnome = 'Fernando' AND sup.unome = 'Wong';

-- d) Funcionários nascidos antes de 1970 e detalhes dos projetos
SELECT f.pnome, p.projnome, p.projlocal, d1.dnome AS dept_func, d2.dnome AS dept_proj, te.horas
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.DEPARTAMENTO d1 ON f.dnr = d1.dnumero
JOIN EMPRESA.TRABALHA_EM te ON f.cpf = te.fcpf
JOIN EMPRESA.PROJETO p ON te.pnr = p.projnumero
JOIN EMPRESA.DEPARTAMENTO d2 ON p.dnum = d2.dnumero
WHERE f.datanasc < '1970-01-01'
ORDER BY f.pnome, p.projnome;

-- e) Nome do funcionário, departamento e se ele é gerente ou está lotado
SELECT f.pnome, d.dnome,
CASE
    WHEN f.cpf = d.cpf_gerente THEN 'Gerente'
    ELSE 'Lotado'
END AS posicao
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.DEPARTAMENTO d ON f.dnr = d.dnumero OR f.cpf = d.cpf_gerente;

-- f) Inserir novo funcionário que trabalhe 15 horas no projeto ProdutoY
INSERT INTO EMPRESA.FUNCIONARIO (cpf, pnome, unome, datanasc, salario, dnr) 
VALUES ('11122233344', 'Carlos', 'Santana', '1985-06-15', 3500, 5);

INSERT INTO EMPRESA.TRABALHA_EM (fcpf, pnr, horas)
VALUES ('11122233344', 2, 15);

-- g) Remover dependentes de João
DELETE FROM EMPRESA.DEPENDENTE
WHERE fcpf = (SELECT cpf FROM EMPRESA.FUNCIONARIO WHERE pnome = 'João');

-- h) Aumentar em 20% as horas de trabalho de André no projeto Informatização
UPDATE EMPRESA.TRABALHA_EM
SET horas = horas * 1.2
WHERE fcpf = (SELECT cpf FROM EMPRESA.FUNCIONARIO WHERE pnome = 'André')
AND pnr = (SELECT projnumero FROM EMPRESA.PROJETO WHERE projnome = 'Informatização');

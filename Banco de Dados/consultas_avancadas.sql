-- 1) Consultas com Subconsultas Aninhadas

-- a) Listar os departamentos onde trabalham os funcionários que nasceram depois de 1960
-- Utilizando IN:
SELECT DISTINCT d.dnome, ld.dlocal
FROM EMPRESA.DEPARTAMENTO d
JOIN EMPRESA.LOCALIZACAO_DEP ld ON d.dnumero = ld.dnumero
WHERE d.dnumero IN (
    SELECT f.dnr
    FROM EMPRESA.FUNCIONARIO f
    WHERE f.datanasc > '1960-01-01'
);

-- Utilizando EXISTS:
SELECT DISTINCT d.dnome, ld.dlocal
FROM EMPRESA.DEPARTAMENTO d
JOIN EMPRESA.LOCALIZACAO_DEP ld ON d.dnumero = ld.dnumero
WHERE EXISTS (
    SELECT 1
    FROM EMPRESA.FUNCIONARIO f
    WHERE f.dnr = d.dnumero
    AND f.datanasc > '1960-01-01'
);

-- b) Mostrar os nomes de departamentos e os nomes dos gerentes desses departamentos que têm funcionários que nasceram antes de 1970
-- Utilizando IN:
SELECT d.dnome, f.pnome AS gerente_nome
FROM EMPRESA.DEPARTAMENTO d
JOIN EMPRESA.FUNCIONARIO f ON d.cpf_gerente = f.cpf
WHERE d.dnumero IN (
    SELECT f2.dnr
    FROM EMPRESA.FUNCIONARIO f2
    WHERE f2.datanasc < '1970-01-01'
)
ORDER BY d.dnome;

-- Utilizando EXISTS:
SELECT d.dnome, f.pnome AS gerente_nome
FROM EMPRESA.DEPARTAMENTO d
JOIN EMPRESA.FUNCIONARIO f ON d.cpf_gerente = f.cpf
WHERE EXISTS (
    SELECT 1
    FROM EMPRESA.FUNCIONARIO f2
    WHERE f2.dnr = d.dnumero
    AND f2.datanasc < '1970-01-01'
)
ORDER BY d.dnome;

-- c) Recupere os nomes de todos os funcionários cujo supervisor do supervisor tenha o nome 'Jorge'
-- Utilizando IN:
SELECT f.pnome
FROM EMPRESA.FUNCIONARIO f
WHERE f.cpf_supervisor IN (
    SELECT f1.cpf
    FROM EMPRESA.FUNCIONARIO f1
    WHERE f1.cpf_supervisor IN (
        SELECT f2.cpf
        FROM EMPRESA.FUNCIONARIO f2
        WHERE f2.pnome = 'Jorge'
    )
);

-- d) Recupere os nomes dos funcionários que ganham mais do que todos os funcionários que trabalham no projeto 'Produto X'
SELECT f.pnome
FROM EMPRESA.FUNCIONARIO f
WHERE f.salario > (
    SELECT MAX(f2.salario)
    FROM EMPRESA.FUNCIONARIO f2
    JOIN EMPRESA.TRABALHA_EM te ON f2.cpf = te.fcpf
    JOIN EMPRESA.PROJETO p ON te.pnr = p.projnumero
    WHERE p.projnome = 'ProdutoX'
);

-- 2) Consultas com Junção e Agrupamento

-- a) Listar os departamentos onde trabalham os funcionários que nasceram depois de 1960
-- Utilizando Junção:
SELECT DISTINCT d.dnome, ld.dlocal
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.DEPARTAMENTO d ON f.dnr = d.dnumero
JOIN EMPRESA.LOCALIZACAO_DEP ld ON d.dnumero = ld.dnumero
WHERE f.datanasc > '1960-01-01';

-- b) Nome do funcionário, nomes dos projetos e horas dedicadas
-- Mesmo que o funcionário não trabalhe em nenhum projeto:
SELECT f.pnome, p.projnome, COALESCE(te.horas, 0) AS horas
FROM EMPRESA.FUNCIONARIO f
LEFT JOIN EMPRESA.TRABALHA_EM te ON f.cpf = te.fcpf
LEFT JOIN EMPRESA.PROJETO p ON te.pnr = p.projnumero;

-- c) Mostrar os nomes de departamentos e os nomes dos gerentes desses departamentos que têm funcionários que nasceram depois de 1960
-- Utilizando Junção:
SELECT DISTINCT d.dnome, f.pnome AS gerente_nome
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.DEPARTAMENTO d ON d.cpf_gerente = f.cpf
JOIN EMPRESA.FUNCIONARIO f2 ON f2.dnr = d.dnumero
WHERE f2.datanasc > '1960-01-01'
ORDER BY d.dnome;

-- d) Recupere os nomes de todos os funcionários cujo supervisor do supervisor tenha o nome 'Jorge'
-- Utilizando Junção:
SELECT f.pnome
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.FUNCIONARIO f1 ON f.cpf_supervisor = f1.cpf
JOIN EMPRESA.FUNCIONARIO f2 ON f1.cpf_supervisor = f2.cpf
WHERE f2.pnome = 'Jorge';

-- e) Apresente os nomes dos projetos que possuem mais de 2 funcionários alocados
SELECT p.projnome
FROM EMPRESA.TRABALHA_EM te
JOIN EMPRESA.PROJETO p ON te.pnr = p.projnumero
GROUP BY p.projnome
HAVING COUNT(te.fcpf) > 2;

-- f) Nome do departamento e número de funcionários onde o salário médio é maior que R$ 3.000,00
SELECT d.dnome, COUNT(f.cpf) AS num_funcionarios
FROM EMPRESA.FUNCIONARIO f
JOIN EMPRESA.DEPARTAMENTO d ON f.dnr = d.dnumero
GROUP BY d.dnome
HAVING AVG(f.salario) > 3000;

-- g) Nome dos funcionários que trabalham no departamento do funcionário com maior salário
SELECT f.pnome
FROM EMPRESA.FUNCIONARIO f
WHERE f.dnr = (
    SELECT f1.dnr
    FROM EMPRESA.FUNCIONARIO f1
    ORDER BY f1.salario DESC
    LIMIT 1
);

-- h) Nome dos funcionários que ganham pelo menos R$ 1.000,00 a mais que o funcionário com o menor salário
SELECT f.pnome
FROM EMPRESA.FUNCIONARIO f
WHERE f.salario >= (
    SELECT MIN(f2.salario) + 1000
    FROM EMPRESA.FUNCIONARIO f2
);

-- Tabela Carro
CREATE TABLE Carro (
    placa VARCHAR(10) PRIMARY KEY,
    chassi VARCHAR(17),
    modelo VARCHAR(50),
    ano_fabricacao INT,
    cor VARCHAR(20)
);

-- Tabela Vendedor
CREATE TABLE Vendedor (
    cpf VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100),
    data_nascimento DATE,
    telefone VARCHAR(20)
);

-- Tabela Acessorio
CREATE TABLE Acessorio (
    codigo VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(100),
    valor DECIMAL(10, 2),
    fabricante VARCHAR(100)
);

-- Tabela Acessorio_do_Carro
CREATE TABLE Acessorio_do_Carro (
    placa_carro VARCHAR(10),
    codigo_acessorio VARCHAR(10),
    quantidade INT,
    PRIMARY KEY (placa_carro, codigo_acessorio),
    FOREIGN KEY (placa_carro) REFERENCES Carro(placa),
    FOREIGN KEY (codigo_acessorio) REFERENCES Acessorio(codigo)
);

-- Tabela Venda
CREATE TABLE Venda (
    placa_carro VARCHAR(10),
    cpf_vendedor VARCHAR(11),
    data DATE,
    valor_total DECIMAL(10, 2),
    PRIMARY KEY (placa_carro, cpf_vendedor, data),
    FOREIGN KEY (placa_carro) REFERENCES Carro(placa),
    FOREIGN KEY (cpf_vendedor) REFERENCES Vendedor(cpf)
);

-- Inserir dados na tabela Carro
INSERT INTO Carro (placa, chassi, modelo, ano_fabricacao, cor) VALUES
('ABC-1234', '123456X', 'Brasília', 1988, 'Vermelho'),
('CDE-4567', '456789Y', 'Fusca', 1986, 'Amarelo');

-- Inserir dados na tabela Vendedor
INSERT INTO Vendedor (cpf, nome, data_nascimento, telefone) VALUES
('111.111.111-11', 'Noemi', '1980-02-01', '(12) 1212-1212'),
('222.222.222-22', 'Zacarias', '1981-03-01', '(13)1313-1313');

-- Inserir dados na tabela Acessorio
INSERT INTO Acessorio (codigo, nome, valor, fabricante) VALUES
('A10', 'Sensor de ré', 200.00, 'F2 Autos'),
('A11', 'Som automotivo', 600.00, 'F3 Eletrônica');

-- Inserir dados na tabela Acessorio_do_Carro
INSERT INTO Acessorio_do_Carro (placa_carro, codigo_acessorio, quantidade) VALUES
('ABC-1234', 'A10', 1);

-- Inserir dados na tabela Venda
INSERT INTO Venda (placa_carro, cpf_vendedor, data, valor_total) VALUES
('ABC-1234', '111.111.111-11', '2022-03-01', 9200.00);


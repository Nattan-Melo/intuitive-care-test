
-- Criação de tabelas

CREATE TABLE relatorio_cadop (
    Registro_ANS VARCHAR(10),
    CNPJ VARCHAR(14),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(50),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(100),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF VARCHAR(2),
    CEP VARCHAR(8),
    DDD VARCHAR(3),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS DATE
);

CREATE TABLE relatorio_contabil (
    DATA DATE,
    REG_ANS VARCHAR(10),
    CD_CONTA_CONTABIL VARCHAR(20),
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(15, 2),
    VL_SALDO_FINAL DECIMAL(15, 2)
);

-- Carregamento dos arquivos .csv para as tabelas criadas
LOAD DATA INFILE 'Relatorio_cadop.csv'
INTO TABLE relatorio_cadop
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '1T2023.csv'
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '2t2023.csv'
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3T2023.csv'  
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;


LOAD DATA INFILE '4T2023.csv'
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;


LOAD DATA INFILE '1T2024.csv'
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;


LOAD DATA INFILE '2T2024.csv'
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3T2024.csv' 
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;


LOAD DATA INFILE '4T2024.csv'
INTO TABLE relatorio_contabil
FIELDS terminated BY ';'
enclosed BY '"'
LINES terminated BY '\n'
IGNORE 1 ROWS;

-- Organização e estruturação de colunas, transformação para convensão

-- Transforma todos os caracters ',' das colunas VL_SALDO_INICIAL e VL_SALDO_FINAL em '.' decimal
UPDATE relatorio_contabil
SET VL_SALDO_INICIAL = replace(VL_SALDO_INICIAL,',','.');

UPDATE relatorio_contabil
SET VL_SALDO_FINAL = replace(VL_SALDO_FINAL,',','.');

-- Padronização para data, substitui todos os '/' para '-'
UPDATE relatorio_contabil
SET DATA = replace(DATA,'/','-');

-- Teste de consulta com data
SELECT STR_TO_DATE(DATA, '%Y-%m-%d') FROM relatorio_contabil
WHERE STR_TO_DATE(DATA, '%Y-%m-%d') = '2024-10-01';


-- 
SELECT DESCRICAO, COUNT(DESCRICAO) as QUANTIDADE FROM relatorio_contabil
GROUP BY DESCRICAO;

SELECT DESCRICAO FROM relatorio_contabil
WHERE DESCRICAO LIKE 'EVENTOS/%' OR DESCRICAO LIKE 'EVENTOS /%';


SELECT DESCRICAO FROM relatorio_contabil
WHERE DESCRICAO LIKE '%SINISTROS CONHECIDOS%';


SELECT DESCRICAO, COUNT(DESCRICAO) as QUANTIDADE FROM relatorio_contabil
WHERE DESCRICAO LIKE '%SINISTROS CONHECIDOS%'
GROUP BY DESCRICAO;

-- Obtem: 10 operadoras com maiores despesas no último trimestre
SELECT REG_ANS, VL_SALDO_INICIAL - VL_SALDO_FINAL as DESPESAS FROM relatorio_contabil
WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND DATA BETWEEN '2024-08-01' AND '2024-10-31'
GROUP BY REG_ANS
ORDER BY DESPESAS DESC
LIMIT 10;

-- 10 operadoras com maiores despesas no último ano
SELECT REG_ANS, VL_SALDO_INICIAL - VL_SALDO_FINAL as DESPESAS FROM relatorio_contabil
WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
AND DATA BETWEEN '01-01-2024' and '2024-12-21'
GROUP BY REG_ANS
ORDER BY DESPESAS DESC
LIMIT 10;





    
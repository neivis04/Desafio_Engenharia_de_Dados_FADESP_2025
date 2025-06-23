-- Criar banco de dados
CREATE DATABASE IF NOT EXISTS bd_fadesp;
USE bd_fadesp;

-- Criar tabela de instituições (dimensão compartilhada)
CREATE TABLE instituicoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_instituicao VARCHAR(255) NOT NULL UNIQUE,
    sigla VARCHAR(20),
    regiao VARCHAR(50),
    uf VARCHAR(5),
    municipio VARCHAR(100),
    capital BOOLEAN
);

-- Tabela com dados do CNPq (dimensão técnica e docente)
CREATE TABLE cnpq_instituicoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    instituicao_id INT,
    ano_censo INT,
    tipo_org_academica INT,
    tipo_rede INT,
    categoria_adm INT,
    qt_doc_total INT,
    qt_tec_total INT,
    FOREIGN KEY (instituicao_id) REFERENCES instituicoes(id)
);

-- Tabela com dados de bolsas do INEP
CREATE TABLE inep_bolsas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    instituicao_id INT,
    ano_referencia INT,
    processo VARCHAR(20),
    data_inicio DATE,
    data_termino DATE,
    beneficiario VARCHAR(255),
    modalidade VARCHAR(100),
    area_conhecimento VARCHAR(150),
    valor_pago DECIMAL(12, 2),
    FOREIGN KEY (instituicao_id) REFERENCES instituicoes(id)
);

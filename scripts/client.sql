CREATE TABLE IF NOT EXISTS public.client
(
    id SERIAL PRIMARY KEY,
    nome character varying(100) NOT NULL,
    cpf character varying(14) NOT NULL UNIQUE,
    rg character varying(20) NOT NULL,
    data_nascimento date NOT NULL,
    cep character varying(10) NOT NULL,
	logradouro character varying(50) NOT NULL,
	complemento character varying(20) NOT NULL,
	bairro character varying(20) NOT NULL,
	cidade character varying(20) NOT NULL,
	estado character varying(2) NOT NULL,
    numero_residencia character varying(5) NOT NULL
);

/*
  PROJETO: Sistema de Gestão de Reservas de Viagens
  DESCRIÇÃO: Consultas com funções de agregação, agrupamento, limitação e ordenação de dados.
  FOCO: Funções matemáticas (COUNT, AVG, SUM, MIN, MAX), agrupamento (GROUP BY), paginação (LIMIT/OFFSET) e ordenação (ORDER BY).
*/

-- =============================================================================
-- 1. FUNÇÕES DE AGREGAÇÃO BÁSICAS E CÁLCULO DE DATAS
-- =============================================================================

SELECT COUNT(*) FROM usuarios;

-- Media da idade dos usuarios
SELECT AVG(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS idade
FROM usuarios;

-- Soma da idade dos usuarios
SELECT SUM(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

-- Menor Idade
SELECT MIN(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

-- Maior Idade
SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS media_idade
FROM usuarios;

-- =============================================================================
-- 2. AGRUPAMENTO DE DADOS (GROUP BY)
-- =============================================================================

-- Calcula quantidade de reservas por destino --
SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino ;


-- =============================================================================
-- 3. PAGINAÇÃO E LIMITAÇÃO DE EXIBIÇÃO (LIMIT / OFFSET)
-- =============================================================================

-- Limit
SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino LIMIT 1 OFFSET 2;

SELECT *, COUNT(*) AS total_reservas FROM reservas GROUP BY id_destino LIMIT 1;

-- =============================================================================
-- 4. ORDENAÇÃO DE RESULTADOS (ORDER BY)
-- =============================================================================

-- Ordenação
SELECT nome
FROM usuarios
ORDER BY nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome;

SELECT nome, data_nascimento
FROM usuarios
ORDER BY data_nascimento, nome DESC;

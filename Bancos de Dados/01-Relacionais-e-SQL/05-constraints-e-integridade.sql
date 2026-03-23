/*
  PROJETO: Sistema de Gestão de Reservas de Viagens
  DESCRIÇÃO: Implementação de restrições (Constraints), Auto-incremento e Integridade Referencial.
  FOCO: Garantia de unicidade e automação de relacionamentos entre tabelas.
*/

-- =============================================================================
-- 1. DEFINIÇÃO DE CHAVES PRIMÁRIAS E AUTO-INCREMENTO
-- =============================================================================

-- Configuração de identificadores automáticos para garantir a unicidade dos registros
ALTER TABLE usuarios
    MODIFY COLUMN id INT AUTO_INCREMENT,
    ADD PRIMARY KEY (id);

ALTER TABLE destinos
    MODIFY COLUMN id INT AUTO_INCREMENT,
    ADD PRIMARY KEY (id);

ALTER TABLE reservas
    MODIFY COLUMN id INT AUTO_INCREMENT,
    ADD PRIMARY KEY (id);

-- =============================================================================
-- 2. TESTE DE INSERÇÃO COM AUTO-INCREMENTO
-- =============================================================================

-- Note que o campo 'id' é omitido, sendo gerenciado automaticamente pelo SGBD
INSERT INTO usuarios (nome, email, data_nascimento, endereco)
VALUES ('João Maria', 'joaomaria@example.com', '1990-01-01', 'Rua A, 123');

INSERT INTO destinos (nome, descricao)
VALUES ('Praia Teste', 'Destino paradisíaco com belas praias.');

INSERT INTO reservas (id_usuario, id_destino, data, status)
VALUES (4, 4, '2023-07-01', 'pendente');

-- =============================================================================
-- 3. INTEGRIDADE REFERENCIAL (FOREIGN KEYS)
-- =============================================================================

-- Estabelecimento de vínculos entre as tabelas de negócio e transações
ALTER TABLE reservas
    ADD CONSTRAINT fk_reservas_usuarios
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id);

ALTER TABLE reservas
    ADD CONSTRAINT fk_reservas_destinos
    FOREIGN KEY (id_destino) REFERENCES destinos(id);

-- =============================================================================
-- 4. EVOLUÇÃO DE REGRAS DE NEGÓCIO (CASCADE)
-- =============================================================================

-- Refatoração da constraint para permitir a remoção automática de reservas 
-- quando um usuário é excluído do sistema (Manutenção de integridade)
ALTER TABLE reservas
    DROP FOREIGN KEY fk_reservas_usuarios;

ALTER TABLE reservas
    ADD CONSTRAINT fk_reservas_usuarios
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
    ON DELETE CASCADE;
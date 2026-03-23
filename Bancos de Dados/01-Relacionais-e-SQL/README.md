# ✈️ Sistema de Gestão de Reservas de Viagens (SQL & ETL)

Este módulo faz parte da trilha de estudos de **Engenharia de Dados**, focado na implementação e evolução de um sistema de banco de dados relacional para gestão de viagens.

O projeto abrange desde a criação inicial do esquema até técnicas avançadas de **Data Wrangling** e **Normalização de Dados**, utilizando padrões da indústria para garantir a integridade e escalabilidade dos dados.

---

## 🛠️ Tecnologias e Conceitos
- **Linguagem**: SQL (Compatível com MySQL/MariaDB)
- **Conceitos de Banco de Dados**:
    - **DDL (Data Definition Language)**: Criação e alteração de estruturas.
    - **DML (Data Manipulation Language)**: Inserção, atualização e exclusão de dados.
    - **DQL (Data Query Language)**: Consultas complexas e filtragem.
    - **Integridade Referencial**: Constraints, Foreign Keys e Auto-incremento.
    - **Refatoração de Schema**: Evolução de tabelas e migração de dados.
    - **Data Wrangling**: Parsing de strings complexas para normalização.

---

## 📂 Estrutura dos Scripts

Os scripts estão organizados por ordem de execução e complexidade:

### 01. [Setup e Inicialização](01-setup-travel-schema.sql)
- Criação das tabelas base: `usuarios`, `destinos` e `reservas`.
- Carga inicial de dados (Seeds) para simulação de ambiente transacional.

### 02. [Consultas e Filtragem](02-consultas-e-filtros.sql)
- Implementação de DQL com foco em performance e projeção de colunas.
- Técnicas de busca por padrão utilizando `LIKE` e wildcards.

### 03. [Manutenção e Escopo](03-manutencao-e-escopo.sql)
- Práticas seguras de `UPDATE` e `DELETE` utilizando chaves únicas.
- Manutenção do ciclo de vida das reservas.

### 04. [Refatoração e Evolução](04-refatoracao-e-evolucao.sql)
- Demonstração de **Blue-Green Deployment** para alteração de tabelas.
- Migração de dados entre estruturas legadas e otimizadas.

### 05. [Constraints e Integridade](05-constraints-e-integridade.sql)
- Implementação de `AUTO_INCREMENT` e Primary Keys.
- Configuração de `ON DELETE CASCADE` para automação de manutenção de integridade.

### 06. [Normalização e Parsing](06-normalizacao-e-parsing.sql)
- **Caso de Uso**: Desmembramento de endereços (string única) em campos atômicos (Rua, Número, Cidade, Estado).
- Uso avançado de `SUBSTRING_INDEX` e `TRIM` para limpeza de dados.

---

## 🚀 Como Executar
1. Certifique-se de ter um ambiente SQL ativo (MySQL/MariaDB recomendado).
2. Execute os scripts sequencialmente (do 01 ao 06) para acompanhar a evolução do projeto.
3. Observe os comentários em cada arquivo para entender as decisões técnicas de implementação.

---

## 📑 Boas Práticas Implementadas
- **Nomenclatura Semântica**: Tabelas e colunas com nomes claros e descritivos.
- **Atomicidade**: Normalização para garantir que cada coluna contenha apenas um dado elementar.
- **Integridade**: Uso rigoroso de Chaves Estrangeiras para evitar órfãos na base de dados.
- **Comentários de Senioridade**: Cada script está documentado com o propósito e a técnica utilizada.

---
*Este repositório serve como portfólio de engenharia de dados e guia de referência para padrões de modelagem SQL.*

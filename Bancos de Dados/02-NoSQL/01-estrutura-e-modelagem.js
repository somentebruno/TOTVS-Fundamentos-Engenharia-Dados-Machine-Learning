/*
  PROJETO: Sistema de Gestão de Reservas de Viagens (Módulo NoSQL)
  DESCRIÇÃO: Primeira modelagem orientada a documentos (JSON/BSON) para Bancos de Dados NoSQL.
  FOCO: Modelagem flat vs sub-documentos (embedded objects) vs arrays de documentos, visando alta flexibilidade sem schemas rígidos.
*/

// =============================================================================
// 1. MODELAGEM: ESTRUTURA PLANA (FLAT)
// =============================================================================

{   
    "_id": "",
    "nome": "nome",
    "data_nascimento": "1990-10-05",
    "email": "pamela.apolinario.borges@gmail.com",
    "endereco": "Av Manoel Marques de Jesus, 380 - Vila Xavier, Araraquara/SP"
}

// =============================================================================
// 2. MODELAGEM: OBJETO EMBUTIDO (EMBEDDED DOCUMENT)
// =============================================================================

// Ou
{   
    "_id": "",
    "nome": "nome",
    "data_nascimento": "1990-10-05",
    "email": "pamela.apolinario.borges@gmail.com",
    "endereco": {
        "rua": "Av Manoel",
        "numero": 123,
        "cidade": "Araraquara",
        "estado": "SP"
    }
}

// =============================================================================
// 3. MODELAGEM: ARRAY DE DOCUMENTOS (ONE-TO-FEW RELATIONSHIP)
// =============================================================================

// ou
{   
    "_id": "",
    "nome": "nome",
    "data_nascimento": "1990-10-05",
    "email": "pamela.apolinario.borges@gmail.com",
    "enderecos": [
        {
        "rua": "Av Manoel",
        "numero": 123,
        "cidade": "Araraquara",
        "estado": "SP"
        },
        {
        "rua": "Av Do estado",
        "numero": 123,
        "cidade": "Araraquara",
        "estado": "SP"
        },
    ]
}

// =============================================================================
// 4. MODELAGEM: COLEÇÃO DE DESTINOS
// =============================================================================

{
    "_id": "",
    "nome": "nome destino",
    "descricao": "Descricao do destino"
}

# Base de Conhecimento

## Dados Utilizados

A base de conhecimento do Fini é composta por arquivos CSV e JSON fictícios/mockados, armazenados na pasta data.

Esses dados são utilizados exclusivamente para fins educacionais e de demonstração. O objetivo é permitir que o agente contextualize suas respostas, utilize exemplos práticos e demonstre como uma IA pode personalizar uma experiência de educação financeira sem acessar dados bancários reais.

| Arquivo | Formato | Para que serve o Fini? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e permitir maior continuidade no atendimento. |
| `perfil_investidor.json` | JSON | Personalizar as explicações de acordo com o perfil, objetivos e informações financeiras fictícias do cliente. |
| `produtos_financeiros.json` | JSON | Disponibilizar informações descritivas sobre produtos financeiros para que o Fini possa explicar seu funcionamento e suas características. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didátAnalisar padrões de receitas e despesas e utilizar essas informações como exemplos didáticos durante as explicações. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto Fundo Imobiliário (FII) substituiu o Fundo Multimercado na base de conhecimento.

A alteração foi realizada porque tenho maior familiaridade com o funcionamento dos Fundos Imobiliários, o que facilita a compreensão e a validação das respostas geradas pelo Fini durante o desenvolvimento do protótipo.

Além disso, a alteração permite trabalhar com um produto de características diferentes dos produtos de renda fixa presentes na base, ampliando os exemplos utilizados pelo agente para fins educacionais.

Importante: a presença de um produto na base de conhecimento não significa que o Fini esteja recomendando sua utilização. Os produtos são utilizados apenas como objetos de estudo e explicação.

---

## Estratégia de Integração

### Como os dados são carregados?
Os dados da base de conhecimento são carregados por código a partir dos arquivos armazenados na pasta data.

Para o protótipo, são utilizados pandas para leitura dos arquivos CSV e o módulo json para leitura dos arquivos JSON.

```python
import pandas as pd
import json

# Arquivos CSV historico = pd.read_csv('data/historico_atendimento.csv') transacoes = pd.read_csv('data/transacoes.csv')

# Arquivos JSON
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f: perfil = json.load(f)
with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f: produtos = json.load(f)
```
Essa abordagem está alinhada com a arquitetura apresentada na Parte 1, na qual os dados são carregados antes da construção do contexto enviado ao modelo de linguagem.

Em uma aplicação mais robusta, os dados poderiam ser consultados dinamicamente de acordo com a pergunta realizada pelo usuário, evitando o envio de informações desnecessárias ao modelo.

---

### Como os dados são usados no prompt?
> Os dados carregados são organizados e sintetizados para formar o contexto da interação.

Esse contexto é enviado ao LLM juntamente com o System Prompt, que contém as regras de comportamento, segurança e anti-alucinação do Fini.

O objetivo é fornecer ao modelo somente as informações relevantes para a resposta, reduzindo o consumo desnecessário de tokens e facilitando a validação das informações utilizadas.

Um exemplo de dados disponíveis no contexto é:

```text
DADOS DO CLIENTE E PERFIL (perfil_investidor.json):

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (transacoes.csv):

data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida


HISTORICO DE ATENDIMENTO AO CLIENTE (historico_atendimento.csv):

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim 2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS FINANCEIROS DISPONÍVEIS PARA EXPLICAÇÃO (produtos_financeiros.json):

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "6% a 12% ao ano",
    "aporte_minimo": 10.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```
Observação sobre os produtos: as informações presentes nessa base são fictícias e foram criadas para o protótipo. O Fini deve utilizá-las para explicar conceitos e características dos produtos, e não para realizar recomendações personalizadas de investimento.
---
## Tratamento de Informações Inconsistentes

>Como o Fini utiliza diferentes fontes de dados, a base pode eventualmente apresentar informações insuficientes ou contraditórias.

Por exemplo, o perfil contém:

"perfil_investidor": "moderado"

e também:

"aceita_risco": false

O agente não deve escolher arbitrariamente uma dessas informações como verdadeira.

De acordo com as regras definidas na Parte 1 e no System Prompt da Parte 3, o Fini deve identificar a inconsistência e solicitar esclarecimento ao usuário antes de utilizar essas informações para uma explicação que dependa dessa definição.

Essa estratégia contribui para reduzir respostas incorretas e evitar que o modelo invente uma interpretação para dados conflitantes.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O contexto abaixo representa uma versão sintetizada dos dados originais da base de conhecimento.

A ideia é disponibilizar ao LLM as informações relevantes para a interação sem necessariamente enviar todos os registros completos dos arquivos.

```
DADOS DO CLIENTE:
- Nome: João Silva
- Idade: 32 anos
- Profissão: Analista de Sistemas
- Renda mensal: R$ 5.000,00
- Perfil informado: Moderado
- Objetivo principal: Construir reserva de emergência
- Patrimônio total: R$ 15.000,00
- Reserva de emergência atual: R$ 10.000,00
- Meta da reserva: R$ 15.000,00

RESUMO DAS TRANSAÇÕES:
- Moradia: R$ 1.380,00
- Alimentação: R$ 570,00
- Transporte: R$ 295,00
- Saúde: R$ 188,00
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

HISTÓRICO RELEVANTE:
- Cliente já perguntou sobre CDB e rentabilidade.
- Cliente já solicitou explicação sobre Tesouro Selic.
- Cliente já acompanhou o progresso da reserva de emergência.

PRODUTOS DISPONÍVEIS PARA EXPLICAÇÃO:
- Tesouro Selic — risco baixo
- CDB Liquidez Diária — risco baixo
- LCI/LCA — risco baixo
- Fundo Imobiliário (FII) — risco médio
- Fundo de Ações — risco alto

REGRAS DE CONTEXTO:
- Utilizar somente as informações fornecidas.
- Não inventar dados.
- Não realizar recomendações de investimentos específicos.
- Identificar informações contraditórias antes de utilizá-las.
- Utilizar os dados para fins educacionais e didáticos.

```
## Por que sintetizar o contexto?

A construção de um contexto resumido permite selecionar as informações mais relevantes para cada interação.

Por exemplo, se o usuário perguntar sobre organização dos gastos, os dados de transações podem ser priorizados.

Se perguntar sobre reserva de emergência, podem ser priorizados o objetivo, o valor atual da reserva, a meta e as informações relacionadas ao histórico de atendimento.

Dessa forma, o contexto pode ser adaptado à pergunta realizada, mantendo a proposta de personalização apresentada na Parte 1.





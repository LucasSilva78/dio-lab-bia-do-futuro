# 🤖 Fini — Agente Financeiro Inteligente

**Projeto desenvolvido no desafio da DIO: Agente Financeiro Inteligente com IA Generativa.**

O Fini é um protótipo de educador financeiro virtual desenvolvido para demonstrar como uma aplicação interativa pode auxiliar iniciantes no aprendizado de educação financeira, na organização de gastos e na compreensão de conceitos financeiros.

O projeto prioriza uma comunicação simples, didática e responsável, com foco em segurança, transparência e prevenção de orientações financeiras inadequadas.

> **Status do projeto:** protótipo funcional em fase inicial, com interface desenvolvida em Streamlit e respostas predefinidas. A integração com um modelo de IA generativa ainda é uma evolução planejada.

---

## 🎯 1. Problema e objetivo

A organização das finanças pessoais pode ser desafiadora para quem está começando a controlar receitas, despesas e objetivos financeiros.

O Fini busca tornar esse aprendizado mais acessível, oferecendo explicações simples e exemplos práticos sobre temas como:

- Reserva de emergência.
- Organização do orçamento pessoal.
- Controle de gastos.
- Conceitos básicos de investimentos.
- Riscos e cuidados na tomada de decisões financeiras.

O objetivo é incentivar hábitos financeiros conscientes por meio de uma experiência interativa e educativa.

## 💡 2. Solução proposta

O Fini foi idealizado como um educador financeiro virtual que utiliza uma comunicação amigável, paciente e didática.

Suas diretrizes incluem:

- Explicar conceitos financeiros em linguagem simples.
- Utilizar exemplos práticos para facilitar o aprendizado.
- Não julgar os hábitos financeiros do usuário.
- Reconhecer os limites das informações disponíveis.
- Não prometer ganhos financeiros.
- Não recomendar a compra de investimentos específicos.
- Incentivar a compreensão dos riscos e o planejamento financeiro.

Na versão atual, esses comportamentos são demonstrados por meio de respostas predefinidas para determinados tipos de perguntas.

## 🛠️ 3. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação da aplicação |
| Streamlit | Desenvolvimento da interface interativa |
| CSV | Armazenamento de dados de exemplo |
| JSON | Organização de informações estruturadas |
| GitHub | Versionamento, documentação e publicação do código |

## 🗂️ 4. Estrutura do repositório

Repositório: [LucasSilva78/dio-lab-bia-do-futuro](https://github.com/LucasSilva78/dio-lab-bia-do-futuro)

Principais diretórios e arquivos:

```text
dio-lab-bia-do-futuro/
├── README.md
├── Pitch_Fini_Projeto_Final_DIO.pptx
├── assets/
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── examples/
└── src/
    ├── README.md
    └── app.py
```

*Observação: a estrutura acima representa a organização prevista para o projeto. Confira os nomes dos arquivos no repositório, pois a listagem deve corresponder aos arquivos efetivamente publicados.*

## 📚 5. Base de conhecimento

O repositório contém arquivos de dados de exemplo que podem apoiar a evolução do agente.

| Arquivo | Formato | Finalidade |
|---|---|---|
| `historico_atendimento.csv` | CSV | Exemplos de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Informações de perfil e preferências |
| `produtos_financeiros.json` | JSON | Informações sobre produtos financeiros |
| `transacoes.csv` | CSV | Exemplos de movimentações financeiras |

A existência desses arquivos não significa que todos estejam conectados à lógica de respostas da aplicação atual. A integração efetiva com a base de conhecimento é uma etapa importante de evolução do projeto.

## 🚀 6. Como executar a aplicação

### Pré-requisitos

- Python instalado no computador.
- Acesso ao repositório do GitHub.
- Conexão com a internet para instalar a dependência.

### Passo 1 — Baixar o projeto

Acesse o [repositório do Fini](https://github.com/LucasSilva78/dio-lab-bia-do-futuro).

Clique em **Code → Download ZIP** e extraia os arquivos para uma pasta do computador.

### Passo 2 — Abrir o PowerShell

Abra a pasta extraída que contém o diretório `src`.

Clique na barra de endereço do Explorador de Arquivos, digite `powershell` e pressione Enter.

### Passo 3 — Instalar o Streamlit

Execute:

```powershell
python -m pip install streamlit
```

### Passo 4 — Executar a aplicação

Na raiz do repositório, execute:

```powershell
python -m streamlit run src/app.py
```

### Passo 5 — Acessar o Fini

Abra no navegador o endereço local apresentado pelo Streamlit, normalmente:

http://localhost:8501

A aplicação é executada localmente no computador. Para disponibilizá-la publicamente na internet, será necessário realizar uma publicação em um serviço de hospedagem.

## 🧪 7. Avaliação e métricas

Foram realizados cinco testes manuais iniciais para verificar o comportamento do protótipo.

| Nº | Cenário avaliado | Resultado relatado |
|---|---|---|
| 1 | Explicação sobre reserva de emergência | Aprovado |
| 2 | Orientações para organizar gastos mensais | Aprovado |
| 3 | Consulta sobre gastos com alimentação | Aprovado |
| 4 | Solicitação de recomendação específica de investimento | Aprovado |
| 5 | Pergunta fora do escopo financeiro | Aprovado |

### Resultados preliminares

- **Testes executados:** 5
- **Testes aprovados:** 5
- **Testes reprovados:** 0
- **Taxa de aprovação funcional observada:** 100%

A taxa representa exclusivamente os cinco cenários testados manualmente. Ela não comprova precisão geral, ausência de alucinações ou segurança em todos os cenários possíveis.

### Métricas propostas para avaliações futuras

- **Assertividade:** verificar se as respostas atendem corretamente às perguntas.
- **Segurança:** avaliar se o agente respeita suas restrições e evita orientações financeiras inadequadas.
- **Coerência:** verificar clareza, consistência e adequação das respostas.
- **Feedback dos usuários:** coletar avaliações de pessoas que testarem a aplicação.

## 🔐 8. Segurança e limitações

O projeto adota a segurança e a transparência como princípios de desenvolvimento.

A versão atual utiliza respostas predefinidas e não possui integração efetiva com um modelo de IA generativa. Por isso, sua capacidade de responder a perguntas é limitada aos comportamentos programados.

Também é importante distinguir a disponibilidade dos arquivos de dados da sua utilização efetiva pela aplicação.

Entre as melhorias planejadas estão:

- Integração com um modelo de IA generativa.
- Recuperação de informações relevantes da base de conhecimento.
- Validação das respostas com base nos dados disponíveis.
- Tratamento de perguntas ambíguas e informações insuficientes.
- Ampliação dos testes estruturados.
- Avaliação por usuários reais.
- Aprimoramento das medidas de segurança e prevenção de respostas incorretas.

## 🎤 9. Pitch do projeto

A apresentação final do projeto está disponível em PowerPoint:

[**Pitch Fini — Projeto Final DIO**](https://github.com/LucasSilva78/dio-lab-bia-do-futuro/blob/main/Pitch_Fini_Projeto_Final_DIO.pptx)

O pitch apresenta o problema identificado, a solução proposta, a demonstração do protótipo e os benefícios esperados da iniciativa.

## 📈 10. Próximos passos

1. Integrar um modelo de IA generativa.
2. Conectar a aplicação aos dados relevantes da base de conhecimento.
3. Implementar mecanismos de validação e controle das respostas.
4. Ampliar os testes de assertividade, segurança e coerência.
5. Obter feedback de usuários reais.
6. Evoluir o protótipo para um agente financeiro educativo mais completo.

## 👨‍💻 11. Conclusão

O Fini representa uma etapa prática de aprendizado no desenvolvimento de aplicações voltadas à educação financeira.

O projeto reúne uma interface interativa, dados estruturados, documentação e testes iniciais, estabelecendo uma base para futuras melhorias e para a integração responsável de IA generativa.

**Fini — Aprender sobre dinheiro é um passo importante para construir um futuro financeiro mais consciente.**












# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste desafio, você vai idealizar e prototipar um agente financeiro que utiliza IA Generativa para:

- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto

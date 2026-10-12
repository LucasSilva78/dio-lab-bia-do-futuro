# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py                # Interface visual e fluxo de chat (Streamlit)
├── agente.py             # Lógica do Agente, RAG em memória e LLM
├── config.py             # Leitura de variáveis de ambiente
└── requirements.txt      # Dependências da aplicação
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Exemplo de src/config.py

```
import os
from dotenv import load_dotenv

# Carrega as variáveis contidas no arquivo .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise ValueError("A chave OPENAI_API_KEY não foi encontrada no arquivo .env")
```

## Exemplo de src/agente.py

```
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME

class AgenteFinanceiro:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        # Base de conhecimento simples em memória sobre finanças/mercado
        self.base_conhecimento = """
        [BASE DE CONHECIMENTO FINANCEIRO]
        1. Regra dos 50/30/20: 50% Renda Fixa/Essencial, 30% Desejos Pessoais, 20% Investimentos e Reserva de Emergência.
        2. Reserva de Emergência: Deve cobrir de 3 a 6 meses de custos fixos em ativos de alta liquidez (ex: Tesouro Selic, CDB 100% CDI).
        3. Renda Fixa: Títulos públicos (Tesouro Direto) e privados (CDB, LCI, LCA). Indicados para perfis conservadores ou objetivos de curto/médio prazo.
        4. Renda Variável: Ações, FIIs (Fundos Imobiliários) e ETFs. Maior risco e potencial de retorno no longo prazo na B3.
        """

    def responder(self, pergunta: str, historico: list) -> str:
        """Gera resposta utilizando a LLM e injetando o contexto da base de conhecimento."""
        system_prompt = (
            "Você é um especialista em análise e inteligência financeira."
            "Responda à dúvida do usuário de forma clara, objetiva e profissional."
            "Utilize como referência primária os seguintes dados da base de conhecimento:\n"
            f"{self.base_conhecimento}"
        )

        messages = [{"role": "system", "content": system_prompt}]
        
        # Adiciona histórico recente para manter o contexto da conversa
        for msg in historico:
            messages.append({"role": msg["role"], "content": msg["content"]})
        
        messages.append({"role": "user", "content": pergunta})

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.3
        )

        return response.choices[0].message.content
```

## Exemplo de src/app.py

```
import streamlit as st
from agente import AgenteFinanceiro

# Configuração da página
st.set_page_config(page_title="Agente Financeiro - DIO", page_icon="💰")
st.title("💰 Agente Financeiro Inteligente")
st.caption("Protótipo Funcional — Streamlit + OpenAI LLM + Base de Conhecimento")

# Inicializa o agente
if "agente" not in st.session_state:
    st.session_state.agente = AgenteFinanceiro()

# Inicializa o histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Sou seu agente financeiro. Como posso ajudar com seus investimentos ou dúvidas financeiras hoje?"}
    ]

# Exibe histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Processa a entrada do usuário
if prompt := st.chat_input("Digite sua pergunta financeira..."):
    # Desenha a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta do agente
    with st.chat_message("assistant"):
        with st.spinner("Consultando base de conhecimento..."):
            resposta = st.session_state.agente.responder(
                pergunta=prompt, 
                historico=st.session_state.messages[:-1]
            )
            st.markdown(resposta)

    # Armazena a resposta no histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})
```

### Como Rodar a Aplicação

1. Crie um arquivo `.env` na raiz do projeto e insira sua chave da OpenAI:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
```

2. Instale as dependências listadas no projeto:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação a partir do diretório raiz do repositório:

```bash
streamlit run src/app.py
```


import streamlit as st
import json
import csv
from pathlib import Path

# Localiza a raiz do repositório
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

st.set_page_config(
    page_title="Fini - Educador Financeiro",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Fini - Educador Financeiro")
st.write(
    "Olá! Sou o Fini. Vou ajudar você a aprender "
    "sobre educação financeira de forma simples e prática."
)

def carregar_json(nome):
    caminho = DATA / nome
    if not caminho.exists():
        return None
    try:
        with caminho.open(encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        return None

def carregar_csv(nome):
    caminho = DATA / nome
    if not caminho.exists():
        return []
    try:
        with caminho.open(
            encoding="utf-8-sig", newline=""
        ) as arquivo:
            return list(csv.DictReader(arquivo))
    except (OSError, csv.Error):
        return []

perfil = carregar_json("perfil_investidor.json")
produtos = carregar_json("produtos_financeiros.json")
historico = carregar_csv("historico_atendimento.csv")
transacoes = carregar_csv("transacoes.csv")

with st.expander("Verificação dos arquivos de dados"):
    st.write("Perfil carregado:", perfil is not None)
    st.write("Produtos carregados:", produtos is not None)
    st.write("Registros de histórico:", len(historico))
    st.write("Registros de transações:", len(transacoes))

st.info(
    "Este protótipo responde a perguntas básicas. "
    "Ele ainda não está conectado a um modelo de IA."
)

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

pergunta = st.chat_input(
    "Pergunte sobre reserva de emergência, gastos ou orçamento..."
)

if pergunta:
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    texto = pergunta.lower()

    if "reserva de emergência" in texto:
        resposta = (
            "A reserva de emergência é um dinheiro guardado "
            "para imprevistos, como um conserto ou uma despesa "
            "inesperada. Comece organizando seu orçamento e "
            "definindo um valor que caiba na sua realidade."
        )
    elif "gastos" in texto or "orçamento" in texto:
        resposta = (
            "Uma boa forma de começar é anotar seus ganhos "
            "e gastos, separar despesas essenciais das "
            "opcionais e revisar o orçamento regularmente. "
            "Não precisa mudar tudo de uma vez!"
        )
    elif "investimento" in texto or "investir" in texto:
        resposta = (
            "Posso ajudar você a entender conceitos e riscos "
            "dos investimentos. Não posso garantir ganhos nem "
            "indicar um investimento específico para comprar. "
            "Vamos começar pelos seus objetivos financeiros?"
        )
    else:
        resposta = (
            "Ainda não tenho uma resposta preparada para essa "
            "pergunta neste protótipo. Tente perguntar sobre "
            "reserva de emergência, gastos, orçamento ou "
            "conceitos de investimento."
        )

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })

    st.rerun()

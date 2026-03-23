import streamlit as st
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sistema de Conferência", layout="wide")

st.markdown("""
<style>
body {
    color: black;
}
.stApp {
    background-color: #f5f5f5;
}
h1, h2, h3, h4, h5, h6, p, label, span {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Sistema Dunexa",
    page_icon="🏢",
    layout="wide"
)

# CORES DA EMPRESA
st.markdown("""
<style>

.stApp {
    background-color: #f2f2f2;
}

h1 {
    color: #5b6f84;
}

.sidebar .sidebar-content {
    background-color: #5b6f84;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("Sistema Dunexa")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Consulta Centro de Custo",
        "Consulta CFOP",
        "Sobre o Sistema"
    ]
)

# CARREGAR PLANILHA
df = pd.read_excel("CENTRO DE CUSTO.xlsx", dtype=str)
df.columns = df.columns.str.strip()
df["CÓDIGO"] = df["CÓDIGO"].astype(str).str.strip()

# MENU PRINCIPAL
if menu == "Consulta Centro de Custo":

    st.title("Consulta de Centro de Custo")

    opcoes = df["CÓDIGO"] + " - " + df["CLIENTE"]

    selecionado = st.selectbox(
        "Selecione o Centro de Custo",
        opcoes
    )

    codigo = selecionado.split(" - ")[0]

    resultado = df[df["CÓDIGO"] == codigo]

    if not resultado.empty:

        linha = resultado.iloc[0]

        st.subheader("Informações do Centro")

        col1, col2, col3 = st.columns(3)

        col1.metric("Cliente", linha["CLIENTE"])
        col2.metric("Tipo de Lançamento", linha["TIPO DE LANÇAMENTO"])
        col3.metric("ICMS", linha["ICMS"])

        col4, col5 = st.columns(2)

        col4.metric("PIS/COFINS", linha["PIS/COFINS"])
        col5.metric("Obra", linha["OBRA"])

elif menu == "Consulta CFOP":

    st.title("Consulta de CFOP")

    cfop = st.text_input("Digite o CFOP da nota")

    if cfop:

        if cfop == "5405":
            st.success("CFOP de entrada sugerido: 1128")

        elif cfop == "5102":
            st.success("CFOP de entrada sugerido: 1102")

        else:
            st.warning("CFOP não cadastrado")

elif menu == "Sobre o Sistema":

    st.title("Sobre")

    st.write("Sistema interno desenvolvido para consulta de centro de custo e CFOP.")
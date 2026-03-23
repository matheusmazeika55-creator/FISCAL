import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sistema Dunexa",
    page_icon="🏢",
    layout="wide"
)

# CORES
st.markdown("""
<style>

.stApp {
    background-color: #f2f2f2;
}

h1,h2,h3,label {
    color: #0B2A45;
}

.stButton>button {
    background-color: #FF3B00;
    color: white;
    border-radius: 8px;
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
        "Sobre"
    ]
)

# CARREGAR PLANILHA
df = pd.read_excel("CENTRO DE CUSTO.xlsx", dtype=str)
df.columns = df.columns.str.strip()
df["CÓDIGO"] = df["CÓDIGO"].str.strip()

# -------------------------
# CENTRO DE CUSTO
# -------------------------

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

        col1,col2,col3 = st.columns(3)

        col1.metric("Cliente", linha["CLIENTE"])
        col2.metric("Tipo de Lançamento", linha["TIPO DE LANÇAMENTO"])
        col3.metric("ICMS", linha["ICMS"])

        col4,col5 = st.columns(2)

        col4.metric("PIS/COFINS", linha["PIS/COFINS"])
        col5.metric("Obra", linha["OBRA"])

# -------------------------
# CFOP
# -------------------------

elif menu == "Consulta CFOP":

    st.title("Consulta CFOP")

    cfop_saida = st.selectbox(
        "CFOP da nota",
        ["5101","6101","5102","6102","6107","6108","5401","6401","5405","6404","5403","6403","5656","6656"]
    )

    tipo = st.selectbox(
        "Tipo da operação",
        [
            "REVENDA",
            "USO E CONSUMO",
            "INDUSTRIALIZAÇÃO",
            "IMOBILIZADO",
            "USO NO SERVIÇO"
        ]
    )

    tabela_cfop = {
        "5405": {
            "USO NO SERVIÇO": "1128"
        },
        "5102": {
            "REVENDA": "1102"
        }
    }

    if cfop_saida in tabela_cfop and tipo in tabela_cfop[cfop_saida]:

        st.success(f"CFOP de entrada: {tabela_cfop[cfop_saida][tipo]}")

    else:

        st.warning("Regra não encontrada")

# -------------------------
# SOBRE
# -------------------------

elif menu == "Sobre":

    st.title("CRIADO POR MATHEUS MAZEIKA")

    st.write("Sistema interno para consulta fiscal.")

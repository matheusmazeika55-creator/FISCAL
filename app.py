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
    st.subheader("Consulta CFOP de Entrada")

cfop_saida = st.selectbox(
    "CFOP da nota",
    [
        "5101","6101",
        "5102","6102",
        "6107","6108",
        "5401","6401",
        "5405","6404","5403","6403",
        "5656","6656"
    ]
)

if cfop_saida and not resultado.empty:

    tipo = linha["TIPO DE LANÇAMENTO"]

    tabela_cfop = {

        "5101": {
            "REVENDA": "1102",
            "USO E CONSUMO": "1556",
            "INDUSTRIALIZAÇÃO": "1104",
            "IMOBILIZADO": "1551",
            "USO NO SERVIÇO": "1128"
        },

        "6101": {
            "REVENDA": "2102",
            "USO E CONSUMO": "2556",
            "INDUSTRIALIZAÇÃO": "2101",
            "IMOBILIZADO": "2551",
            "USO NO SERVIÇO": "2128"
        },

        "5102": {
            "REVENDA": "1102",
            "USO E CONSUMO": "1556",
            "INDUSTRIALIZAÇÃO": "1104",
            "IMOBILIZADO": "1551",
            "USO NO SERVIÇO": "1128"
        },

        "6102": {
            "REVENDA": "2102",
            "USO E CONSUMO": "2557",
            "INDUSTRIALIZAÇÃO": "2102",
            "IMOBILIZADO": "2552",
            "USO NO SERVIÇO": "2128"
        },

        "5401": {
            "REVENDA": "1403",
            "USO E CONSUMO": "1407",
            "INDUSTRIALIZAÇÃO": "1401",
            "IMOBILIZADO": "1406",
            "USO NO SERVIÇO": "1128"
        },

        "6401": {
            "REVENDA": "2403",
            "USO E CONSUMO": "2407",
            "INDUSTRIALIZAÇÃO": "2401",
            "IMOBILIZADO": "2406",
            "USO NO SERVIÇO": "2128"
        },

        "5405": {
            "REVENDA": "1403",
            "USO E CONSUMO": "1407",
            "INDUSTRIALIZAÇÃO": "1401",
            "IMOBILIZADO": "1406",
            "USO NO SERVIÇO": "1128"
        },

        "6404": {
            "REVENDA": "2403",
            "USO E CONSUMO": "2407",
            "INDUSTRIALIZAÇÃO": "2401",
            "IMOBILIZADO": "2406",
            "USO NO SERVIÇO": "2128"
        }
    }

    if cfop_saida in tabela_cfop:

        tipo_limpo = tipo.replace("E_", "").strip()

        if tipo_limpo in tabela_cfop[cfop_saida]:

            cfop_entrada = tabela_cfop[cfop_saida][tipo_limpo]

            st.success(f"CFOP de entrada: {cfop_entrada}")

        else:
            st.warning("Tipo de operação não encontrado na regra")

    else:
        st.warning("CFOP não cadastrado na tabela")

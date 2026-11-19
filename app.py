import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Censo - 1872", layout="wide")
st.sidebar.header("Controles")
opcao = st.sidebar.radio(["Tabela")

df = pd.read_csv("censo_1872.csv")
FONTE_DADOS = "hardcoded"
ARQUIVO = "censo_1872.xlsx"

def carregar_dados(): "censo_1872.xlsx"

arr.sum() = df.columns = "total",
df.drop_duplicates(),
arr.sum("homens_livres", "homens_escravizados", "mulheres_livres", "mulheres_escravizados")

  st.subheader("Gráfico de Pizza")
    fig_pizza = px.pie(
        dados_pizza,
        names="Censo",         
        values=COL_VALOR,            
        title=f"Censo demográfico de ({1872})",
        color="Categoria",
        color_discrete_map=CORES,
        template=TEMPLATE,
    )

    fig_pizza.update_traces(textinfo="percent+label+value")
    mostrar(estilizar(fig_pizza))

        st.subheader("Gráfico de Radar")
    fig_radar = px.line_polar(
        dados_radar,
        r="Nota",                    
        theta="Dimensao",            
        color="Categoria",              
        line_close=True,             
        title=f"Perfil Multidimensional (Gráfico de censo demográfico - {1872})",
        color_discrete_map=CORES,
        template=TEMPLATE,
    )
    fig_radar.update_traces(fill="toself")   

    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])))
    mostrar(estilizar(fig_radar))
    
    st.markdown("---")    
st.caption("Fonte dos dados: Censo Demográfico de 1872 — https://basedosdados.org/")
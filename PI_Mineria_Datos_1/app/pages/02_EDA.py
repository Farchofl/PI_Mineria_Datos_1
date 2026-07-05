import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")

st.title("📈 Etapa 3: Análisis Exploratorio de Datos (EDA)")


# --- CARGA DE DATOS (CORREGIDA) ---
@st.cache_data
def load_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "streaming_users_clean (2).json")
    return pd.read_json(file_path)


df = load_data()


# --- UNIVARIADO ---
st.subheader("1. Análisis Univariado")
c1, c2 = st.columns(2)

with c1:
    st.write("Distribución de edad")
    fig1 = px.histogram(df, x="edad")
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.write("Distribución de ingresos")
    fig2 = px.box(df, y="ingresos")
    st.plotly_chart(fig2, use_container_width=True)


# --- BIVARIADO ---
st.subheader("2. Análisis Bivariado")
c3, c4 = st.columns(2)

with c3:
    st.write("Edad vs Ingresos")
    fig3 = px.scatter(df, x="edad", y="ingresos")
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    st.write("Suscripción por edad")
    fig4 = px.bar(df, x="edad", color="suscripcion")
    st.plotly_chart(fig4, use_container_width=True)


# --- MULTIVARIADO ---
st.subheader("3. Análisis Multivariado")

fig5 = px.scatter_matrix(df, dimensions=["edad", "ingresos"])
st.plotly_chart(fig5, use_container_width=True)
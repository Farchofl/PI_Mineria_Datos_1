import streamlit as st

# ----------------------------
# Configuración de la página
# ----------------------------
st.set_page_config(
    page_title="Proyecto Integrador - Minería de Datos 1",
    page_icon="🕶️",
    layout="wide"
)

# ----------------------------
# Título principal
# ----------------------------
st.title(" Proyecto Integrador - Minería de Datos 1")

st.markdown("### Análisis Exploratorio y Reducción de Dimensionalidad")

st.divider()

# ----------------------------
# Información general
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader(" Integrante")
    st.write("- Fabricio Fabian Loza")
    

    st.subheader("🎓 Comisión")
    st.write("Completar")

with col2:
    st.subheader("jueves 2 ")
    st.write("Julio 2026")

    st.subheader(" Materia")
    st.write("Minería de Datos 1")

st.divider()

# ----------------------------
# Contexto
# ----------------------------
st.header(" Contexto del Proyecto")

st.write("""
Este proyecto fue desarrollado para la materia **Minería de Datos 1**.

El objetivo consiste en analizar un conjunto de datos aplicando las distintas
etapas del proceso de minería de datos:

- Inspección inicial del dataset.
- Limpieza y preparación de los datos.
- Análisis Exploratorio de Datos (EDA).
- Reducción de dimensionalidad mediante PCA.
- Presentación de resultados mediante una aplicación desarrollada en Streamlit.
""")

st.divider()

# ----------------------------
# Navegación
# ----------------------------
st.header(" Navegación")

st.info("""
Utilice el menú lateral para acceder a las diferentes secciones del proyecto:

• Dataset

• EDA

• PCA

• Conclusiones
""")

st.divider()

# ----------------------------
# Repositorio
# ----------------------------
st.header("🔗 Repositorio del Proyecto")

st.markdown(
    """
**GitHub:**

https://github.com/Farchofl/PI_Mineria_Datos_1
"""
)

st.success("La aplicación fue desarrollada utilizando Python y Streamlit.")

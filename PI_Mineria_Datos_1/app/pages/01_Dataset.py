import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="📊", layout="wide")

st.title("📊 Etapa 2: Análisis del Dataset")

# 1. Carga de datos
@st.cache_data
def load_data():
    return pd.read_json("streaming_users_clean (2).json")

try:
    df = load_data()
    
    # 2. Métricas rápidas
    col1, col2, col3 = st.columns(3)
    col1.metric("Registros", df.shape[0])
    col2.metric("Variables", df.shape[1])
    col3.metric("Valores Nulos", df.isnull().sum().sum())

    st.divider()

    # 3. Vista previa
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head(10), use_container_width=True)

    # 4. Calidad de datos
    st.subheader("Calidad de datos")
    buffer = df.dtypes.to_frame(name='Tipo de dato').join(
        df.isnull().sum().to_frame(name='Nulos')
    )
    st.table(buffer)

except Exception as e:
    st.error(f"Error al cargar el archivo: {e}")



    import os
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Obtiene la ruta de la carpeta raíz (donde está el JSON)
    # Suponiendo que el JSON está al mismo nivel que la carpeta 'app'
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_path, "streaming_users_clean (2).json")
    return pd.read_json(file_path)
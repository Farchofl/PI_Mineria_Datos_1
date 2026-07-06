import streamlit as st
import pandas as pd
from pathlib import Path

# ----------------------------------------------------
# Configuración
# ----------------------------------------------------

st.set_page_config(
page_title="Dataset",
page_icon="📁",
layout="wide"
)

# ----------------------------------------------------
# Ruta del proyecto
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

archivo = BASE_DIR / "data" / "processed" / "dataset_final.csv"

# ----------------------------------------------------
# Cargar dataset
# ----------------------------------------------------

df = pd.read_csv(archivo)

# ----------------------------------------------------
# Título
# ----------------------------------------------------

st.title("📁 Dataset")

st.write("""
En esta sección se presenta una descripción general del conjunto de datos
utilizado durante el Proyecto Integrador.

Se muestran sus principales características estructurales con el propósito
de proporcionar una visión inicial antes de avanzar hacia el Análisis
Exploratorio de Datos (EDA) y las etapas posteriores del proceso de minería
de datos.
""")

st.divider()

# ----------------------------------------------------
# Información general
# ----------------------------------------------------

st.header("📊 Información general")

registros = len(df)
variables = len(df.columns)
numericas = len(df.select_dtypes(include="number").columns)
categoricas = len(df.select_dtypes(exclude="number").columns)
faltantes = df.isnull().sum().sum()

calidad = (
df.notnull().sum().sum()
/ (df.shape[0] * df.shape[1])
) * 100

c1, c2, c3 = st.columns(3)

with c1:
st.metric("📄 Registros", registros)
st.metric("🏷️ Variables categóricas", categoricas)

with c2:
st.metric("🧩 Variables totales", variables)
st.metric("🚨 Valores faltantes", faltantes)

with c3:
st.metric("🔢 Variables numéricas", numericas)
st.metric("✅ Calidad de datos", f"{calidad:.2f}%")

st.info(
f"El conjunto de datos contiene {df.shape[0]} registros y {df.shape[1]} variables."
)

st.divider()

# ----------------------------------------------------
# Estadísticas descriptivas
# ----------------------------------------------------

st.header("📈 Estadísticas descriptivas")

st.write("""
La siguiente tabla resume las principales medidas descriptivas de las
variables numéricas del conjunto de datos.
""")

st.dataframe(df.describe())

st.divider()

# ----------------------------------------------------
# Valores faltantes
# ----------------------------------------------------

st.header("🚨 Valores faltantes")

nulos = df.isnull().sum()
nulos = nulos[nulos > 0]

if len(nulos) > 0:
st.dataframe(
nulos.to_frame(
name="Cantidad de valores faltantes"
)
)

st.warning(
"Se detectaron variables con valores faltantes que fueron tratadas durante la etapa de preparación de datos."
)

else:
st.success("No existen valores faltantes en el dataset procesado.")

st.divider()

# ----------------------------------------------------
# Vista previa
# ----------------------------------------------------

st.header("👀 Vista previa del dataset")

cantidad = st.selectbox(
"Seleccione la cantidad de filas a visualizar",
[5, 10, 15, 20]
)

st.dataframe(df.head(cantidad))

st.divider()

# ----------------------------------------------------
# Variables del dataset
# ----------------------------------------------------

st.header("📝 Variables del dataset")

tipos = pd.DataFrame({
"Variable": df.columns,
"Tipo de dato": df.dtypes.astype(str)
})

st.dataframe(tipos)

st.divider()

# ----------------------------------------------------
# Transformaciones realizadas
# ----------------------------------------------------

st.header("🔄 Transformaciones principales")

st.info("""
Durante el desarrollo del proyecto se realizaron las siguientes tareas de
preparación de datos:

• Eliminación de registros duplicados.

• Tratamiento de valores faltantes.

• Corrección de inconsistencias detectadas en las variables.

• Normalización de variables categóricas.

• Verificación de tipos de datos.

• Generación del dataset procesado utilizado posteriormente en el Análisis
Exploratorio de Datos (EDA) y en el Análisis de Componentes Principales (PCA).
""")

st.divider()

# ----------------------------------------------------
# Conclusión
# ----------------------------------------------------

st.header("✅ Conclusión")

st.success("""
La revisión inicial del conjunto de datos permitió verificar su estructura,
identificar los tipos de variables presentes y evaluar su calidad general.

El dataset procesado se encuentra en condiciones adecuadas para continuar con
las etapas de Análisis Exploratorio de Datos (EDA) y Análisis de Componentes
Principales (PCA), que permitirán comprender con mayor profundidad el
comportamiento de las variables y las relaciones existentes entre ellas.
""")


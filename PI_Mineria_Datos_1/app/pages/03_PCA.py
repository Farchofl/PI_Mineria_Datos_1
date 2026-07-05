import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt

st.title("Reducción de Dimensionalidad (PCA)")

df = pd.read_json(r"E:\PI_Minería_Datos_1\PI_Minería_Datos_1\data\processed\streaming_users_clean (2).json")

# Selección de variables numéricas
X = df.select_dtypes(include=['float64','int64'])

# Escalamiento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

st.write("Varianza explicada por los componentes:", pca.explained_variance_ratio_)

fig, ax = plt.subplots()
ax.scatter(X_pca[:,0], X_pca[:,1])
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
st.pyplot(fig)

st.markdown("Interpretación: El PCA permite visualizar la estructura de los datos en dos dimensiones, capturando la mayor parte de la varianza.")
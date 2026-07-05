# Proyecto de Minería de Datos

## Información general
Este proyecto corresponde a la materia Minería de Datos.  
Se desarrolla en modalidad grupal y abarca inspección inicial, limpieza, análisis exploratorio, reducción de dimensionalidad y conclusiones.  
Incluye repositorio público en GitHub, aplicación en Streamlit Cloud, informe final y registro ETL.

## Objetivo del proyecto
Analizar un dataset de usuarios de plataformas de streaming para identificar patrones de consumo, evaluar la calidad de los datos, aplicar técnicas de reducción de dimensionalidad y comunicar hallazgos relevantes.  
El objetivo es comprender el comportamiento de los usuarios y proponer próximos pasos de análisis.  

## Dataset
El dataset original se encuentra en `data/raw/`.  
El dataset limpio y procesado está en `data/processed/streaming_users_clean (2).json`.  
Contiene información sobre edad, género, tipo de suscripción y horas de streaming.  
Se preserva el archivo original sin modificaciones y se documentan las transformaciones en el log ETL.  

## Estructura del repositorio
- `data/raw/`: dataset original.  
- `data/processed/`: dataset final.  
- `notebooks/`: desarrollo de inspección, limpieza, EDA, PCA y conclusiones.  
- `app/`: aplicación pública en Streamlit.  
- `reports/`: informe final en PDF.  
- `logs/`: registro ETL.  
- `README.md`: documentación técnica.  
- `requirements.txt`: dependencias necesarias.  

## Preparación y calidad de datos
Se eliminaron valores nulos y duplicados.  
Se normalizaron variables numéricas y se codificaron variables categóricas.  
Se documentaron todas las transformaciones en `logs/pipeline_log.csv`.  
El dataset final preserva la estructura y permite reproducibilidad.  

## Resumen del análisis exploratorio
Se realizaron visualizaciones univariadas, bivariadas y multivariadas.  
Se identificaron patrones de consumo según edad y tipo de suscripción.  
Se observó relación entre horas de streaming y características demográficas.  
Los resultados se encuentran en `notebooks/03_eda.ipynb` y en la aplicación Streamlit.  

## Reducción de dimensionalidad
Se aplicó PCA sobre variables numéricas con escalamiento previo.  
Los dos primeros componentes explican gran parte de la varianza.  
Resultados disponibles en `notebooks/04_pca.ipynb` y en la aplicación Streamlit.  

## Visualización interactiva
La aplicación en Streamlit incluye:  
- Vista del dataset.  
- EDA con 5 visualizaciones.  
- PCA con interpretación y visualizaciones.  
- Conclusiones generales.  
Enlace: [Aplicación en Streamlit Cloud](https://streamlit.io)  

## Cómo ejecutar localmente
1. Clonar el repositorio.  
2. Instalar dependencias:  
   ```bash
   pip install -r requirements.txt
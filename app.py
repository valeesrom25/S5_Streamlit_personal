import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Exploración de Datos",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploración de Datos con Correlación")
st.write("Sube un archivo CSV para analizar sus datos.")

# Subida de archivo
archivo = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if archivo is not None:
    try:
        # Leer CSV
        df = pd.read_csv(archivo)

        # Mensaje de éxito
        st.success("✅ Archivo cargado correctamente")

        # Mostrar primeras filas
        st.subheader("Vista previa de los datos (df.head())")
        st.dataframe(df.head())

        # Información general
        st.subheader("Información del dataset")
        st.write(f"Filas: {df.shape[0]}")
        st.write(f"Columnas: {df.shape[1]}")

        # Seleccionar columnas numéricas
        columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()

        if len(columnas_numericas) >= 2:

            st.subheader("Selecciona columnas para correlación")

            columnas_seleccionadas = st.multiselect(
                "Columnas numéricas",
                columnas_numericas,
                default=columnas_numericas[:2]
            )

            if len(columnas_seleccionadas) >= 2:

                # Matriz de correlación
                correlacion = df[columnas_seleccionadas].corr()

                st.subheader("Matriz de correlación")
                st.dataframe(correlacion)

                # Crear gráfico
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.heatmap(
                    correlacion,
                    annot=True,
                    cmap='coolwarm',
                    fmt='.2f',
                    linewidths=0.5,
                    ax=ax
                )

                ax.set_title("Mapa de calor de correlación")

                st.pyplot(fig)

            else:
                st.warning("⚠️ Selecciona al menos 2 columnas.")

        else:
            st.warning("⚠️ El archivo necesita al menos 2 columnas numéricas.")

    except Exception as e:
        st.error(f"❌ Error al cargar el archivo: {e}")

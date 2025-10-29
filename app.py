from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Vehículos", layout="wide")

# Ruta robusta: siempre carga el CSV desde la carpeta del archivo app.py
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "vehicles_us.csv"

# Carga de datos con manejo de error
try:
    car_data = pd.read_csv(CSV_PATH)
except FileNotFoundError:
    st.error(f"No encuentro el archivo: {CSV_PATH}")
    st.stop()

# Encabezado
st.header("Exploración de datos de vehículos")

# Primer botón: histograma
build_histogram = st.checkbox("Construir histograma")

if build_histogram:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Segundo botón: gráfico de dispersión
build_scatter = st.checkbox("Construir gráfico de dispersión")

if build_scatter:
    st.write(
        "Creación de un gráfico de dispersión entre el precio y el kilometraje del vehículo")
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title="Relación entre kilometraje y precio")
    st.plotly_chart(fig2, use_container_width=True)

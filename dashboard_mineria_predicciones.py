
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial
st.set_page_config(page_title="Visión futura de la minería", layout="wide")
st.title("🔍 Tablero Interactivo - La Minería y sus Visiones a Futuro")
st.markdown("Análisis del sector minero colombiano: producción, precios, predicciones y oportunidades.")

# Datos simulados (con base en los archivos originales proporcionados)
volumenes = pd.DataFrame({
    "Año": [2020, 2021, 2022, 2023, 2024],
    "Mineral": ["Carbón", "Carbón", "Cobre", "Cobre", "Oro"],
    "Producción": [85, 90, 40, 45, 60]
})

carbon = pd.DataFrame({
    "Año": [2020, 2021, 2022, 2023, 2024, 2025],
    "Producción_mill_ton": [90, 88, 75, 60, 50, 45],
    "Precio_usd": [120, 150, 400, 200, 120, 100]
})

base3 = pd.DataFrame({
    "Mineral": ["Cobre", "Litio", "Níquel", "Oro", "Carbón"],
    "Demanda_Proyectada": [95, 80, 60, 40, 20]
})

# Menú lateral
menu = st.sidebar.radio("Selecciona una vista:", [
    "📊 Producción Histórica",
    "📉 Análisis del Carbón",
    "🔮 Proyecciones Futuras",
    "📈 Predicciones del Mercado",
    "📌 Recomendaciones Estratégicas"
])

# Vista de Producción
if menu == "📊 Producción Histórica":
    st.subheader("Producción Histórica por Mineral")
    mineral = st.selectbox("Selecciona un mineral:", volumenes["Mineral"].unique())
    datos = volumenes[volumenes["Mineral"] == mineral]
    fig = px.line(datos, x="Año", y="Producción", markers=True,
                  title=f"Producción de {mineral} por Año")
    st.plotly_chart(fig, use_container_width=True)

# Vista del Carbón
elif menu == "📉 Análisis del Carbón":
    st.subheader("Producción y Precio del Carbón (2020–2025)")
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(carbon, x="Año", y="Producción_mill_ton", title="Producción de Carbón")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.line(carbon, x="Año", y="Precio_usd", title="Precio del Carbón (USD/Ton)")
        st.plotly_chart(fig2, use_container_width=True)

# Vista de Proyecciones
elif menu == "🔮 Proyecciones Futuras":
    st.subheader("Proyecciones de Demanda por Mineral (2025–2030)")
    st.markdown("- 📉 **Reducción del 30%** en producción de carbón térmico.")
    st.markdown("- 📈 **Cobre y litio** crecerán por demanda tecnológica.")
    st.markdown("- 🟢 **Formalización minera** aumentará en zonas PDET.")
    fig = px.bar(base3, x="Mineral", y="Demanda_Proyectada", color="Mineral",
                 title="Demanda Proyectada a 2030")
    st.plotly_chart(fig, use_container_width=True)

# Vista de Predicciones del Mercado
elif menu == "📈 Predicciones del Mercado":
    st.subheader("Predicciones y Comportamiento del Mercado Minero")
    st.markdown("### 🔮 Predicciones Clave (2025–2030)")
    st.markdown("""
    - **Producción de carbón** seguirá cayendo por presión ambiental y descarbonización global.
    - **Cobre** se posicionará como mineral clave para infraestructura eléctrica y transporte.
    - **Litio y níquel** crecerán con el auge de vehículos eléctricos y almacenamiento de energía.
    - **La inversión extranjera** puede disminuir si persisten incertidumbres regulatorias.
    - **La formalización minera** aumentará con incentivos del gobierno y presión internacional.
    """)
    fig = px.line(carbon, x="Año", y="Producción_mill_ton",
                  title="Tendencia Proyectada: Producción de Carbón Térmico")
    st.plotly_chart(fig, use_container_width=True)
    st.info("Estas predicciones se basan en tendencias reales, objetivos de transición energética y análisis de mercado desde 2020.")

# Vista de Recomendaciones
elif menu == "📌 Recomendaciones Estratégicas":
    st.subheader("Recomendaciones para un Futuro Minero Sostenible")
    st.markdown("""
    ### 👨‍👩‍👧‍👦 Para comunidades:
    - Participar activamente en proyectos mineros responsables.

    ### 🏛️ Para el gobierno:
    - Garantizar seguridad jurídica e incentivos sostenibles.

    ### 💼 Para inversionistas:
    - Apostar por cobre, níquel y litio para transición energética.

    ### 🧪 Para la academia:
    - Promover innovación en tecnologías limpias y trazabilidad.
    """)
    st.info("Fuente: Proyecto Aula + análisis de mercado minero 2020–2025")

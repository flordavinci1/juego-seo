import streamlit as st
import pandas as pd

# ---- Configuración de página ----
st.set_page_config(page_title="Auditoría SEO Interactiva", page_icon="🔍", layout="wide")

# ---- Estado inicial ----
if "nivel" not in st.session_state:
    st.session_state.nivel = 1
if "resultados" not in st.session_state:
    st.session_state.resultados = {}

# ---- Funciones ----
def siguiente_nivel():
    st.session_state.nivel += 1

def mostrar_progreso():
    progreso = (st.session_state.nivel - 1) / 5
    st.progress(progreso)
    mensajes = [
        "🚀 ¡Empezamos el viaje SEO!",
        "🛠 Optimizando como profesionales...",
        "🌐 Construyendo autoridad...",
        "✍️ Planificando el contenido...",
        "🏆 ¡Misión completada!"
    ]
    st.markdown(f"**{mensajes[st.session_state.nivel - 1]}**")

# ---- Header ----
st.title("🔍 Auditoría SEO Interactiva")
st.markdown("Completa cada nivel para desbloquear el siguiente y obtener tu plan SEO. **¡Gana puntos mientras avanzas!**")

# ---- Barra de progreso ----
mostrar_progreso()

# ---- Nivel 1: Datos básicos ----
if st.session_state.nivel == 1:
    st.header("📌 Nivel 1: Datos básicos")
    url = st.text_input("🌍 URL del sitio o competidor")
    industria = st.text_input("🏭 Industria / Nicho")
    publico = st.text_area("🎯 Público objetivo")

    if st.button("Siguiente ➡️", type="primary"):
        if url and industria and publico:
            st.session_state.resultados.update({
                "URL": url,
                "Industria": industria,
                "Público objetivo": publico
            })
            siguiente_nivel()
        else:
            st.warning("Completa todos los campos para continuar.")

# ---- Nivel 2: On-page SEO ----
elif st.session_state.nivel == 2:
    st.header("🛠 Nivel 2: On-page SEO")
    col1, col2 = st.columns(2)
    with col1:
        titulos = st.checkbox("Títulos y metadescripciones optimizados")
        headers = st.checkbox("Uso correcto de encabezados (H1, H2, H3...)")
    with col2:
        imagenes = st.checkbox("Imágenes con texto alternativo")
        enlazado = st.checkbox("Estructura de enlaces internos correcta")

    if st.button("Siguiente ➡️", type="primary"):
        st.session_state.resultados.update({
            "Títulos optimizados": titulos,
            "Encabezados correctos": headers,
            "Imágenes optimizadas": imagenes,
            "Enlaces internos correctos": enlazado
        })
        siguiente_nivel()

# ---- Nivel 3: Off-page SEO ----
elif st.session_state.nivel == 3:
    st.header("🌐 Nivel 3: Off-page SEO")
    backlinks = st.text_input("🔗 Cantidad aproximada de backlinks")
    autoridad = st.slider("📊 Autoridad del dominio", 0, 100, 0)
    menciones = st.text_area("📰 Menciones / colaboraciones relevantes")

    if st.button("Siguiente ➡️", type="primary"):
        st.session_state.resultados.update({
            "Backlinks": backlinks,
            "Autoridad de dominio": autoridad,
            "Menciones relevantes": menciones
        })
        siguiente_nivel()

# ---- Nivel 4: Contenido y estrategia ----
elif st.session_state.nivel == 4:
    st.header("✍️ Nivel 4: Contenido y estrategia")
    keywords = st.text_area("🔑 Principales palabras clave objetivo")
    calendario = st.text_area("🗓 Propuesta de calendario editorial")
    tono = st.selectbox("🎤 Tono de comunicación", ["Formal", "Informal", "Técnico", "Amigable"])

    if st.button("Finalizar ✅", type="primary"):
        st.session_state.resultados.update({
            "Palabras clave": keywords,
            "Calendario editorial": calendario,
            "Tono de comunicación": tono
        })
        siguiente_nivel()

# ---- Nivel 5: Resumen ----
elif st.session_state.nivel == 5:
    st.header("🏆 Resumen de la auditoría SEO")
    st.success("¡Felicidades! Has completado la auditoría SEO.")
    
    df = pd.DataFrame(st.session_state.resultados.items(), columns=["Elemento", "Valor"])
    st.table(df)

    # Descargar CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar resultados en CSV",
        data=csv,
        file_name="auditoria_seo.csv",
        mime="text/csv"
    )
    
    st.balloons()

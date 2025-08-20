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
        "🚀 ¡Arranquemos con la auditoría!",
        "🛠 Revisando metadatos...",
        "📖 Analizando semántica y tópicos...",
        "🌐 Midiendo reputación y visibilidad...",
        "🏆 ¡Listo! Tenés tu estrategia SEO."
    ]
    st.markdown(f"**{mensajes[st.session_state.nivel - 1]}**")

# ---- Header ----
st.title("🔍 Auditoría SEO Interactiva")
st.markdown("Completa cada nivel para desbloquear el siguiente y obtener tu plan SEO. **¡Gana puntos mientras avanzas!**")

# ---- Barra de progreso ----
mostrar_progreso()

# ---- Nivel 1: Infraestructura técnica ----
if st.session_state.nivel == 1:
    st.header("📌 Nivel 1: Infraestructura técnica")
    url = st.text_input("🌍 URL del sitio o competidor")
    robots = st.checkbox("✅ El sitio tiene robots.txt accesible")
    sitemap = st.checkbox("✅ El sitio tiene sitemap.xml accesible")
    errores404 = st.checkbox("❌ Encontraste errores 404")
    status200 = st.checkbox("✅ La mayoría de las páginas devuelven código 200 (OK)")

    if st.button("Siguiente ➡️", type="primary"):
        if url:
            st.session_state.resultados.update({
                "URL": url,
                "Robots.txt": robots,
                "Sitemap.xml": sitemap,
                "Errores 404": errores404,
                "Status 200 OK": status200
            })
            siguiente_nivel()
        else:
            st.warning("Por favor, ingresa al menos la URL.")

# ---- Nivel 2: On-page SEO ----
elif st.session_state.nivel == 2:
    st.header("🛠 Nivel 2: Metadatos y estructura on-page")
    title = st.checkbox("✅ Titles optimizados")
    meta = st.checkbox("✅ Metadescripciones completas")
    headers = st.checkbox("✅ Encabezados jerarquizados (H1, H2, H3)")
    imagenes = st.checkbox("✅ Imágenes con texto alternativo (ALT)")

    if st.button("Siguiente ➡️", type="primary"):
        st.session_state.resultados.update({
            "Titles optimizados": title,
            "Metadescripciones completas": meta,
            "Encabezados jerarquizados": headers,
            "Imágenes con ALT": imagenes
        })
        siguiente_nivel()

# ---- Nivel 3: Semántica y relevancia ----
elif st.session_state.nivel == 3:
    st.header("📖 Nivel 3: Relevancia semántica")
    topicos = st.text_area("📚 Principales tópicos detectados en el sitio")
    coherencia = st.selectbox("🎯 Comunicación alineada con marca/industria", ["Sí", "Parcial", "No"])
    keywords = st.text_area("🔑 Palabras clave identificadas (keyword research)")
    relevancia = st.slider("📊 Nivel de relevancia semántica (1-10)", 1, 10, 5)

    if st.button("Siguiente ➡️", type="primary"):
        st.session_state.resultados.update({
            "Tópicos principales": topicos,
            "Coherencia comunicacional": coherencia,
            "Palabras clave": keywords,
            "Relevancia semántica (1-10)": relevancia
        })
        siguiente_nivel()

# ---- Nivel 4: Reputación y visibilidad ----
elif st.session_state.nivel == 4:
    st.header("🌐 Nivel 4: Reputación y visibilidad")
    menciones = st.text_area("📰 Personas hablando de la marca (`mi marca -site:midominio.com`)")
    backlinks = st.text_input("🔗 Backlinks / menciones externas (aprox.)")
    presencia = st.text_area("📢 Presencia en medios, foros o redes sociales")
    gsc = st.text_area("📊 Keywords desde Google Search Console (si hay acceso)")

    if st.button("Siguiente ➡️", type="primary"):
        st.session_state.resultados.update({
            "Menciones externas": menciones,
            "Backlinks": backlinks,
            "Presencia en medios/redes": presencia,
            "Keywords desde GSC": gsc
        })
        siguiente_nivel()

# ---- Nivel 5: Estrategia ----
elif st.session_state.nivel == 5:
    st.header("🏆 Nivel 5: Estrategia SEO")
    mejoras_tecnicas = st.text_area("🛠 Lista de mejoras técnicas prioritarias")
    mejoras_onpage = st.text_area("🔑 Acciones sobre metadatos y on-page")
    plan_contenidos = st.text_area("📝 Estrategia de contenidos (keywords + tópicos)")
    branding = st.text_area("📢 Acciones de branding / reputación digital")

    if st.button("Finalizar ✅", type="primary"):
        st.session_state.resultados.update({
            "Mejoras técnicas": mejoras_tecnicas,
            "Acciones on-page": mejoras_onpage,
            "Plan de contenidos": plan_contenidos,
            "Acciones de branding": branding
        })
        siguiente_nivel()

# ---- Resumen final ----
elif st.session_state.nivel == 6:
    st.header("📊 Resumen de la auditoría SEO")
    st.success("¡Felicidades! Has completado toda la auditoría. 🎉")

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

import streamlit as st

st.set_page_config(page_title="Auditoría SEO Educativa", layout="wide")

st.title("🔍 Auditoría SEO Educativa")
st.markdown("Guía paso a paso para revisar un sitio web en clase. Completá cada casilla para avanzar.")

# --- 1. Requisitos básicos ---
st.header("1. Requisitos básicos")
with st.expander("Checklist de requisitos"):
    robots = st.checkbox("📄 Revisar `robots.txt`")
    sitemap = st.checkbox("🗺️ Revisar `sitemap.xml`")
    meta = st.checkbox("🏷️ Revisar metadatos (title y meta descriptions)")
    screaming = st.checkbox("🛠️ Usar Screaming FLOR para diagnóstico")

# --- 2. Errores técnicos ---
st.header("2. Errores técnicos")
with st.expander("Checklist de errores técnicos"):
    errores_404 = st.checkbox("❌ Revisar errores 404")
    codigos_200 = st.checkbox("✅ Confirmar que la mayoría de las páginas responden con 200")
    navegacion = st.checkbox("🧭 Revisar que la navegación no muestre errores")

# --- 3. Relevancia semántica ---
st.header("3. Relevancia semántica")
with st.expander("Checklist de semántica"):
    topicos = st.checkbox("📚 Revisar que el sitio esté orientado a los tópicos correctos")
    alineacion = st.checkbox("📝 Confirmar alineación entre comunicación y objetivos")
    keyword = st.checkbox("🔑 Realizar Keyword Research inicial")
    gsc = st.checkbox("📊 Revisar datos de Google Search Console (si hay acceso)")

# --- 4. Presencia y reputación ---
st.header("4. Presencia y reputación")
with st.expander("Checklist de marca"):
    menciones = st.checkbox("🗣️ Buscar menciones de la marca con `mi marca -site:midominio.com`")
    reputacion = st.checkbox("🌍 Revisar si hay conversaciones externas sobre la marca")

# --- 5. Observaciones finales ---
st.header("5. Observaciones finales")
observaciones = st.text_area("✏️ Anotaciones o hallazgos importantes")

# --- Resumen ---
st.header("📌 Resumen de auditoría")
if st.button("Generar resumen"):
    st.subheader("Checklist completado:")
    
    if robots: st.write("✔️ Revisado robots.txt")
    if sitemap: st.write("✔️ Revisado sitemap.xml")
    if meta: st.write("✔️ Revisados metadatos")
    if screaming: st.write("✔️ Usado Screaming FLOR")
    if errores_404: st.write("✔️ Revisados errores 404")
    if codigos_200: st.write("✔️ Confirmada navegación con códigos 200")
    if navegacion: st.write("✔️ Navegación sin errores")
    if topicos: st.write("✔️ Revisada orientación a tópicos correctos")
    if alineacion: st.write("✔️ Comunicación alineada")
    if keyword: st.write("✔️ Keyword research inicial realizado")
    if gsc: st.write("✔️ Revisados datos de GSC")
    if menciones: st.write("✔️ Revisadas menciones externas")
    if reputacion: st.write("✔️ Presencia y reputación verificadas")

    if observaciones:
        st.subheader("📝 Observaciones")
        st.write(observaciones)

import streamlit as st

st.set_page_config(page_title="Auditoría SEO Educativa", layout="wide")

st.title("🔍 Auditoría SEO Educativa")
st.markdown("Guía paso a paso para revisar un sitio web en clase. Completá cada casilla para avanzar.")

# --- URL del sitio ---
st.header("🔗 URL a auditar")
url = st.text_input("Ingresá la URL del sitio web que vas a revisar")

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

# --- Resumen y sugerencias estratégicas ---
st.header("📌 Resumen de auditoría y recomendaciones")
if st.button("Generar resumen"):
    if url:
        st.subheader(f"✅ Auditoría del sitio: {url}")
    else:
        st.subheader("✅ Auditoría del sitio (URL no ingresada)")

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

    # --- Sugerencias estratégicas automáticas ---
    st.subheader("🎯 Sugerencias estratégicas automáticas")
    sugerencias = []

    # Recomendaciones según checklist
    if not robots:
        sugerencias.append("✅ Revisar y configurar `robots.txt` para controlar la indexación.")
    if not sitemap:
        sugerencias.append("✅ Generar y subir `sitemap.xml` para mejorar la indexación.")
    if not meta:
        sugerencias.append("✅ Optimizar titles y meta descriptions para mejorar CTR y relevancia.")
    if not errores_404:
        sugerencias.append("✅ Corregir errores 404 para mejorar la experiencia de usuario y SEO.")
    if not codigos_200:
        sugerencias.append("✅ Asegurar que la mayoría de las páginas respondan con 200 OK.")
    if not navegacion:
        sugerencias.append("✅ Revisar navegación y enlaces internos para evitar errores.")
    if not topicos:
        sugerencias.append("✅ Redefinir contenidos para orientar el sitio a los tópicos correctos.")
    if not alineacion:
        sugerencias.append("✅ Ajustar la comunicación y objetivos del contenido para coherencia estratégica.")
    if not keyword:
        sugerencias.append("✅ Realizar un keyword research inicial para guiar la creación de contenido.")
    if not gsc:
        sugerencias.append("✅ Conectar con Google Search Console para monitorizar rendimiento y errores.")
    if not menciones:
        sugerencias.append("✅ Analizar menciones de la marca para identificar oportunidades de presencia online.")
    if not reputacion:
        sugerencias.append("✅ Revisar reputación online y responder a feedback si aplica.")

    if sugerencias:
        for s in sugerencias:
            st.write(s)
    else:
        st.write("✔️ Todos los aspectos revisados. Continuar con implementación de mejoras y estrategia avanzada.")

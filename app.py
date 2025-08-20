import streamlit as st

st.set_page_config(page_title="Auditoría SEO Educativa", layout="wide")

st.title("🔍 Auditoría SEO Educativa Interactiva")
st.markdown("Las recomendaciones aparecen según tus respuestas y se acumulan automáticamente en el panel lateral como plan de acción SEO.")

# --- URL del sitio ---
st.header("🔗 URL a auditar")
url = st.text_input("Ingresá la URL del sitio web que vas a revisar")

# --- Lista para acumular sugerencias ---
plan_accion = []

# --- Función para mostrar checkbox y acumular sugerencias ---
def checkbox_sugerencia(pregunta, debe_tener, mensaje):
    respuesta = st.checkbox(pregunta)
    if (debe_tener and not respuesta) or (not debe_tener and respuesta):
        plan_accion.append(mensaje)
    return respuesta

# --- 1. Requisitos básicos ---
st.header("1. Requisitos básicos")
robots = checkbox_sugerencia(
    "📄 ¿Tiene robots.txt?", True, 
    "✅ Revisar y configurar robots.txt si no existe."
)
sitemap = checkbox_sugerencia(
    "🗺️ ¿Tiene sitemap.xml?", True, 
    "✅ Generar y subir sitemap.xml para mejorar la indexación."
)
meta = checkbox_sugerencia(
    "🏷️ ¿Tiene title y meta descriptions optimizadas?", True, 
    "✅ Optimizar titles y meta descriptions para mejorar CTR y relevancia."
)
screaming = checkbox_sugerencia(
    "🛠️ ¿Se realizó un diagnóstico con Screaming FLOR?", True, 
    "✅ Realizar análisis con Screaming FLOR para identificar errores técnicos."
)

# --- 2. Errores técnicos ---
st.header("2. Errores técnicos")
errores_404 = checkbox_sugerencia(
    "❌ ¿Tiene errores 404?", False, 
    "✅ Corregir errores 404 para mejorar la experiencia de usuario y SEO."
)
codigos_200 = checkbox_sugerencia(
    "✅ ¿La mayoría de las páginas responden con 200 OK?", True, 
    "✅ Asegurar que la mayoría de las páginas respondan correctamente."
)
navegacion = checkbox_sugerencia(
    "🧭 ¿La navegación funciona correctamente?", True, 
    "✅ Revisar enlaces internos y menús para evitar errores."
)

# --- 3. Relevancia semántica ---
st.header("3. Relevancia semántica")
topicos = checkbox_sugerencia(
    "📚 ¿El sitio está orientado a los tópicos correctos?", True, 
    "✅ Redefinir contenidos para orientar el sitio a los tópicos correctos."
)
alineacion = checkbox_sugerencia(
    "📝 ¿La comunicación está alineada con objetivos?", True, 
    "✅ Ajustar la comunicación y objetivos del contenido para coherencia estratégica."
)
keyword = checkbox_sugerencia(
    "🔑 ¿Se realizó keyword research inicial?", True, 
    "✅ Realizar un keyword research inicial para guiar la creación de contenido."
)
gsc = checkbox_sugerencia(
    "📊 ¿Se revisan datos de Google Search Console?", True, 
    "✅ Conectar con Google Search Console para monitorizar rendimiento y errores."
)

# --- 4. Presencia y reputación ---
st.header("4. Presencia y reputación")
menciones = checkbox_sugerencia(
    "🗣️ ¿Se buscan menciones de la marca?", True, 
    "✅ Analizar menciones de la marca para identificar oportunidades online."
)
reputacion = checkbox_sugerencia(
    "🌍 ¿Se revisa la reputación online?", True, 
    "✅ Revisar reputación online y responder a feedback si aplica."
)

# --- 5. Observaciones finales ---
st.header("5. Observaciones finales")
observaciones = st.text_area("✏️ Anotaciones o hallazgos importantes")

# --- Panel lateral con plan de acción acumulado ---
st.sidebar.header("🎯 Plan de acción SEO acumulado")
if plan_accion:
    for a in plan_accion:
        st.sidebar.write(a)
else:
    st.sidebar.write("Todas las verificaciones cumplen con los requisitos. Avanzá con la estrategia avanzada.")

# --- Resumen final ---
st.header("📌 Resumen de auditoría")
if st.button("Generar resumen final"):
    if url:
        st.subheader(f"✅ Auditoría del sitio: {url}")
    else:
        st.subheader("✅ Auditoría del sitio (URL no ingresada)")

    st.subheader("Checklist resumido:")
    checklist = [
        ("robots.txt", robots),
        ("sitemap.xml", sitemap),
        ("Metadatos", meta),
        ("Screaming FLOR", screaming),
        ("Errores 404", errores_404),
        ("Códigos 200", codigos_200),
        ("Navegación", navegacion),
        ("Tópicos", topicos),
        ("Alineación de comunicación", alineacion),
        ("Keyword research", keyword),
        ("Google Search Console", gsc),
        ("Menciones", menciones),
        ("Reputación", reputacion),
    ]
    for item, valor in checklist:
        st.write(f"✔️ {item}: {'Sí' if valor else 'No'}")

    if observaciones:
        st.subheader("📝 Observaciones")
        st.write(observaciones)

    if plan_accion:
        st.subheader("🎯 Recomendaciones estratégicas acumuladas")
        for a in plan_accion:
            st.write(a)
    else:
        st.write("✔️ Todas las verificaciones cumplen con los requisitos. Continuar con estrategia avanzada.")

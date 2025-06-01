import streamlit as st

st.set_page_config(page_title="Centro Culinario", layout="wide")

st.title("Bienvenidos al Centro de Capacitación en Cocina 👨‍🍳")
st.markdown("""
Ofrecemos cursos profesionales de cocina para todos los niveles.  
Descubre nuestro plan de estudios, beneficios y metodología.
""")

st.header("📘 Plan de Estudios")
st.markdown("""
- Cocina Básica
- Cocina Internacional
- Pastelería
- Nutrición y Manipulación de Alimentos
""")

st.header("🤖 Chatbot de Inscripciones")
st.markdown("Puedes resolver tus dudas o iniciar tu inscripción aquí:")

# Incrustar el chatbot de Landbot (iframe)
landbot_url = "https://landbot.online/v3/H-2971594-YFSU7IQBD0ZX8MJV/index.html"
st.components.v1.iframe(landbot_url, height=600, scrolling=True)

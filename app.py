import streamlit as st
import streamlit.components.v1 as components

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
st.markdown("Puedes resolver tus dudas o iniciar tu inscripción a través del botón flotante de chat en la esquina inferior de la pantalla.")

# Código JavaScript para Landbot Popup
landbot_popup_script = """
<script>
window.addEventListener('mouseover', initLandbot, { once: true });
window.addEventListener('touchstart', initLandbot, { once: true });
var myLandbot;
function initLandbot() {
  if (!myLandbot) {
    var s = document.createElement('script');
    s.type = "module";
    s.async = true;
    s.addEventListener('load', function() {
      myLandbot = new Landbot.Popup({
        configUrl: 'https://storage.googleapis.com/landbot.online/v3/H-2971594-YFSU7IQBD0ZX8MJV/index.json',
      });
    });
    s.src = 'https://cdn.landbot.io/landbot-3/landbot-3.0.0.mjs';
    var x = document.getElementsByTagName('script')[0];
    x.parentNode.insertBefore(s, x);
  }
}
</script>
"""

# Incrustar el script dentro del HTML
components.html(landbot_popup_script, height=0, width=0)

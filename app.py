import streamlit as st
import random

# Charger les décimales de pi
@st.cache_data
def charger_pi():
    with open("pi.txt", "r") as f:
        return f.read().strip()

pi_decimales = charger_pi()

# Initialisation de session_state
if 'suite_affichee' not in st.session_state:
    st.session_state.suite_affichee = ""
if 'validation_suite' not in st.session_state:
    st.session_state.validation_suite = ""

# 🎨 Titre
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>🧠 Pi Trainer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Mémorise les décimales de π ! Complète la suite quand tu es prêt.</p>", unsafe_allow_html=True)
st.divider()

# Choix de la plage
fin = st.number_input(
    "🔢 Jusqu’à quelle position de décimales veux-tu t'entraîner ?",
    min_value=20,
    max_value=len(pi_decimales),
    value=100
)

# Bouton pour générer une nouvelle suite
if st.button("🎲 Générer une nouvelle suite"):
    plage = pi_decimales[0:fin]
    if len(plage) < 15:
        st.warning("Pas assez de décimales dans la plage.")
    else:
        index_depart = random.randint(0, len(plage) - 15)
        index_arrive = index_depart + 5
        st.session_state.suite_affichee = plage[index_depart:index_arrive]
        st.session_state.validation_suite = plage[index_arrive:index_arrive + 10]

# Affichage de la suite
if st.session_state.suite_affichee:
    st.markdown(f"### 🔍 Complète la suite après : `{st.session_state.suite_affichee}`")

    with st.form(key="validation_form"):
        user_input = st.text_input(
            "Entre les 10 décimales suivantes :",
            value="",
            max_chars=10
        )
        submitted = st.form_submit_button("Valider")

    if submitted:
        if len(user_input) != 10 or not user_input.isdigit():
            st.error("❌ Entrée invalide. Tu dois entrer exactement 10 chiffres.")
            st.info(f"✅ La bonne suite était : `{st.session_state.validation_suite}`")
        elif user_input == st.session_state.validation_suite:
            st.success("✅ Correct ! Bien joué 👏")
            st.balloons()
            st.session_state.suite_affichee = ""
            st.session_state.validation_suite = ""
        else:
            for i in range(10):
                if user_input[i] != st.session_state.validation_suite[i]:
                    st.error(f"❌ Erreur à la position {i+1} : tu as mis '{user_input[i]}' au lieu de '{st.session_state.validation_suite[i]}'")
                    break
            st.info(f"📌 La bonne suite était : `{st.session_state.validation_suite}`")
else:
    st.info("Clique sur '🎲 Générer une nouvelle suite' pour commencer !")

import streamlit as st
import random

st.set_page_config(layout="wide")

# Charger les décimales de pi
@st.cache_data
def charger_pi():
    with open("pi.txt", "r") as f:
        return f.read().strip()

pi_decimales = charger_pi()

# Onglets
onglets = st.tabs(["🔢 Entraînement", "📖 Lecture"])

# ===========
# ONGLET 1 : Entraînement
# ===========
with onglets[0]:
    st.markdown("<h1 style='text-align:center; color:#4CAF50;'>🧠 Pi Trainer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Mémorise les décimales de π ! Complète la suite quand tu es prêt.</p>", unsafe_allow_html=True)
    st.divider()

    if 'suite_affichee' not in st.session_state:
        st.session_state.suite_affichee = ""
    if 'validation_suite' not in st.session_state:
        st.session_state.validation_suite = ""

    fin = st.number_input(
        "🔢 Jusqu'à quelle position de décimales veux-tu t'entraîner ?",
        min_value=20,
        max_value=len(pi_decimales),
        value=100
    )

    if st.button("🎲 Générer une nouvelle suite"):
        plage = pi_decimales[0:fin]
        if len(plage) < 15:
            st.warning("Pas assez de décimales dans la plage.")
        else:
            index_depart = random.randint(0, len(plage) - 15)
            index_arrive = index_depart + 5
            st.session_state.suite_affichee = plage[index_depart:index_arrive]
            st.session_state.validation_suite = plage[index_arrive:index_arrive + 10]

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


with onglets[1]:
    st.markdown("""
        <h2 style='text-align: center; color: #2196F3; margin-bottom: 1em;'>
            📘 Lecture des 100 000 premières décimales de π
        </h2>
    """, unsafe_allow_html=True)
    st.divider()


    suite = st.session_state.get("suite_affichee", "")
    pi_100k = pi_decimales[:100000]


    # Surlignage : insérer la balise AVANT de faire les blocs
    if suite and suite in pi_100k:
        pi_100k = pi_100k.replace(
            suite,
            f"<span style='background-color: yellow; font-weight: bold'>{suite}</span>",
            1  # seulement la première occurrence
        )

    # Construction des lignes avec 100 chiffres (ou moins si balises HTML)
    lignes = []
    current_index = 0
    display_index = 0

    while current_index < len(pi_100k):
        bloc = ""
        bloc_length = 0
        i = current_index

        # Compter les chiffres visibles (en ignorant les balises HTML)
        while i < len(pi_100k) and bloc_length < 100:
            if pi_100k[i] == "<":
                end_tag = pi_100k.find(">", i)
                bloc += pi_100k[i:end_tag + 1]
                i = end_tag + 1
            else:
                bloc += pi_100k[i]
                bloc_length += 1
                i += 1

        current_index = i

        # Diviser le bloc en 10 morceaux de 10 chiffres
        chiffres_purs = ""
        tmp = bloc
        while "<" in tmp:
            pre = tmp[:tmp.find("<")]
            chiffres_purs += pre
            tmp = tmp[tmp.find(">")+1:]
        chiffres_purs += tmp
        blocs = []
        index_chiffre = 0
        for _ in range(10):
            sous_bloc = ""
            chiffre_count = 0
            while index_chiffre < len(bloc) and chiffre_count < 10:
                if bloc[index_chiffre] == "<":
                    # Copier balise HTML
                    end_tag = bloc.find(">", index_chiffre)
                    sous_bloc += bloc[index_chiffre:end_tag+1]
                    index_chiffre = end_tag + 1
                else:
                    sous_bloc += bloc[index_chiffre]
                    chiffre_count += 1
                    index_chiffre += 1
            blocs.append(sous_bloc)

        ligne_formatee = "    ".join(blocs)
        lignes.append(f"{str(display_index).zfill(6)} : {ligne_formatee}")
        display_index += 100

    contenu_html = "<br>".join(lignes)

    st.markdown(
        f"""
        <div style="
            overflow-x: auto;
            white-space: nowrap;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            line-height: 1.6;
            background-color: #f9f9f9;
            padding: 16px;
            border: 1px solid #ddd;
            border-radius: 8px;
            max-height: 600px;
            overflow-y: scroll;
        ">
            {contenu_html}
        </div>
        """,
        unsafe_allow_html=True
    )

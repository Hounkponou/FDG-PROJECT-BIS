import streamlit as st
from load_data import load_data
from process_data import process_data
from model import build_model
from recommandation import recommend_numbers


# Appliquer le style CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown("""<link rel="stylesheet" type="text/css" href="./static/css/style.css">""", unsafe_allow_html=True)


# Charger le style CSS
local_css("static/css/style_streamlit.css")


# Fonction pour la page de saisie de la date
def date_input_page():
    st.title("Prévisions de Tirage de Loterie")
    st.image("static/img/lottery.jpg", width=500, use_column_width=True, output_format='JPEG')
    st.write("Entrez la date du prochain tirage pour obtenir des recommandations de numéros.")

    date_input = st.text_input("Date (ddmmyyyy):", "")

    if st.button("Soumettre"):
        if len(date_input) == 8 and date_input.isdigit():
            st.session_state.date_input = date_input
            st.session_state.page = "Résultats"
            st.experimental_rerun()
        else:
            st.error("Format de date invalide. Veuillez utiliser 'ddmmyyyy'.")


# Fonction pour la page des résultats
def results_page():
    if 'date_input' in st.session_state:
        st.title('Résultat possible du tirage')
        st.image("static/img/results.jpg", width=500)
        date_input = st.session_state.date_input
        date = date_input[:2] + '/' + date_input[2:4] + '/' + date_input[4:8]
        df = load_data()
        df = process_data(df)
        knn = build_model(df)
        recommendation = recommend_numbers(knn, date)
        recommendation = [str(x) for x in recommendation]

        st.subheader(f"Recommandations pour le {date}")
        st.markdown(f"""
        - **Boule 1 **: {recommendation[0]}
        - **Boule 2 **: {recommendation[1]}
        - **Boule 3 **: {recommendation[2]}
        - **Boule 4 **: {recommendation[3]}
        - **Boule 5 **: {recommendation[4]}
        - **Étoile 1 **: {recommendation[5]}
        - **Étoile 2 **: {recommendation[6]}
        """)

        st.balloons()

        if st.button("Recommencer"):
            st.session_state.page = "Entrer la date"
            st.experimental_rerun()

    else:
        st.error("Veuillez d'abord entrer une date dans la section 'Entrer la date'.")
        st.session_state.page = "Entrer la date"
        st.experimental_rerun()


# Fonction principale
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "Entrer la date"

    if st.session_state.page == "Entrer la date":
        date_input_page()
    elif st.session_state.page == "Résultats":
        results_page()


if __name__ == "__main__":
    main()

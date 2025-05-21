import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
# streamlit run my_second_website.py

# Données utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'toto',
            'password': 'totoMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Setup de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

# Affichage du widget d'authentification sur la page du site
authenticator.login()


def accueil():
    st.title("Bienvenue sur le site de Guillaume")
    st.image("https://www.longislandpress.com/wp-content/uploads/2013/06/gatsby1.jpg")


def photo():
    st.title("Voici mes photos de Pandas")
    # Création de 3 colonnes
    col1, col2, col3 = st.columns(3)

    # Contenu de la première colonne :
    with col1:
        st.header("Un Panda")
        st.image("https://miro.medium.com/v2/resize:fit:1200/1*aiZ9jyv_7cAqSZ7OTZw4ug.jpeg")

    # Contenu de la deuxième colonne :
    with col2:
        st.header("Un Panel Data")
        st.image("https://miro.medium.com/v2/resize:fit:1080/1*fUO28EIHi1bkZPhjZ451tQ.jpeg")

    # Contenu de la troisième colonne :
    with col3:
        st.header("Des bébés Pandas")
        st.image("https://images.rtl.fr/~c/2000v2000/rtl/www/1523992-les-bebes-pandas-du-zoo-de-beauval.jpg")


if st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
else:
    # Le bouton de déconnexion
    with st.sidebar:
        st.write(f'Bienvenue {st.session_state.get("name")}')
        selection = option_menu(
                menu_title=None,
                options=["Accueil", "Photos"],
            )
    authenticator.logout("Déconnexion", location="sidebar")

    if selection == "Accueil":
        accueil()
    elif selection == "Photos":
        photo()

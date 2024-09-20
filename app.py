import streamlit as st
from streamlit_option_menu import option_menu

# Ustawienie tytułu aplikacji
st.title("Przykładowa Strona z Nawigacją")

# Pasek nawigacyjny z rozwijanym menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",  # Tytuł menu
        options=["Strona Główna", "O Nas", "Usługi"],  # Opcje w menu
        icons=["house", "info-circle", "tools"],  # Ikony dla opcji
        menu_icon="cast",  # Ikona menu
        default_index=0,  # Domyślna wybrana opcja
    )

# Treść na podstawie wybranej opcji
if selected == "Strona Główna":
    st.subheader("Witamy na stronie głównej!")
    st.write("To jest treść strony głównej.")
    
elif selected == "O Nas":
    st.subheader("O Nas")
    st.write("Informacje o firmie.")
    
elif selected == "Usługi":
    st.subheader("Nasze Usługi")
    st.write("Opis oferowanych usług.")


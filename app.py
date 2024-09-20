import streamlit as st
from streamlit_option_menu import option_menu

# Funkcje do wyświetlania zawartości strony głównej i podstron
def strona_glowna():
    st.title("Tytuł strony głównej")
    st.write("Treść strony głównej")

def podstrona(tytul, tresc):
    st.title(tytul)
    st.write(tresc)

# Menu główne z trzema opcjami
with st.sidebar:
    opcja = option_menu(
        menu_title=None,
        options=["Opcja 1", "Opcja 2", "Opcja 3"],
        icons=["list", "list", "list"],  # Możesz dostosować ikony
        orientation="horizontal",
        default_index=0,
    )

# Rozwijane podmenu dla każdej opcji
if opcja == "Opcja 1":
    podopcja = option_menu(
        menu_title="Wybierz podmenu:",
        options=["Podopcja 1.1", "Podopcja 1.2", "Podopcja 1.3"],
        icons=["caret-right", "caret-right", "caret-right"],
        orientation="vertical"
    )
    if podopcja == "Podopcja 1.1":
        podstrona("Tytuł podstrony 1.1", "Treść podstrony 1.1")
    elif podopcja == "Podopcja 1.2":
        podstrona("Tytuł podstrony 1.2", "Treść podstrony 1.2")
    elif podopcja == "Podopcja 1.3":
        podstrona("Tytuł podstrony 1.3", "Treść podstrony 1.3")

elif opcja == "Opcja 2":
    podopcja = option_menu(
        menu_title="Wybierz podmenu:",
        options=["Podopcja 2.1", "Podopcja 2.2", "Podopcja 2.3"],
        icons=["caret-right", "caret-right", "caret-right"],
        orientation="vertical"
    )
    if podopcja == "Podopcja 2.1":
        podstrona("Tytuł podstrony 2.1", "Treść podstrony 2.1")
    elif podopcja == "Podopcja 2.2":
        podstrona("Tytuł podstrony 2.2", "Treść podstrony 2.2")
    elif podopcja == "Podopcja 2.3":
        podstrona("Tytuł podstrony 2.3", "Treść podstrony 2.3")

elif opcja == "Opcja 3":
    podopcja = option_menu(
        menu_title="Wybierz podmenu:",
        options=["Podopcja 3.1", "Podopcja 3.2", "Podopcja 3.3"],
        icons=["caret-right", "caret-right", "caret-right"],
        orientation="vertical"
    )
    if podopcja == "Podopcja 3.1":
        podstrona("Tytuł podstrony 3.1", "Treść podstrony 3.1")
    elif podopcja == "Podopcja 3.2":
        podstrona("Tytuł podstrony 3.2", "Treść podstrony 3.2")
    elif podopcja == "Podopcja 3.3":
        podstrona("Tytuł podstrony 3.3", "Treść podstrony 3.3")

# Domyślnie strona główna
if opcja == "Opcja 1" and 'podopcja' not in locals():
    strona_glowna()

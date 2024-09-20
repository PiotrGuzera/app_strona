import streamlit as st

# Funkcja do wyświetlania zawartości podstron
def display_page(title, content):
    st.title(title)
    st.write(content)

# Główna nawigacja z trzema opcjami
menu = st.selectbox('Menu', ['Strona główna', 'Opcja 1', 'Opcja 2', 'Opcja 3'])

# Zawartość dla każdej opcji
if menu == 'Strona główna':
    display_page('Tytuł strony głównej', 'Treść strony głównej')
elif menu == 'Opcja 1':
    submenu = st.selectbox('Podmenu Opcja 1', ['Podstrona 1.1', 'Podstrona 1.2', 'Podstrona 1.3'])
    if submenu == 'Podstrona 1.1':
        display_page('Tytuł podstrony 1.1', 'Treść podstrony 1.1')
    elif submenu == 'Podstrona 1.2':
        display_page('Tytuł podstrony 1.2', 'Treść podstrony 1.2')
    elif submenu == 'Podstrona 1.3':
        display_page('Tytuł podstrony 1.3', 'Treść podstrony 1.3')
elif menu == 'Opcja 2':
    submenu = st.selectbox('Podmenu Opcja 2', ['Podstrona 2.1', 'Podstrona 2.2', 'Podstrona 2.3'])
    if submenu == 'Podstrona 2.1':
        display_page('Tytuł podstrony 2.1', 'Treść podstrony 2.1')
    elif submenu == 'Podstrona 2.2':
        display_page('Tytuł podstrony 2.2', 'Treść podstrony 2.2')
    elif submenu == 'Podstrona 2.3':
        display_page('Tytuł podstrony 2.3', 'Treść podstrony 2.3')
elif menu == 'Opcja 3':
    submenu = st.selectbox('Podmenu Opcja 3', ['Podstrona 3.1', 'Podstrona 3.2', 'Podstrona 3.3'])
    if submenu == 'Podstrona 3.1':
        display_page('Tytuł podstrony 3.1', 'Treść podstrony 3.1')
    elif submenu == 'Podstrona 3.2':
        display_page('Tytuł podstrony 3.2', 'Treść podstrony 3.2')
    elif submenu == 'Podstrona 3.3':
        display_page('Tytuł podstrony 3.3', 'Treść podstrony 3.3')

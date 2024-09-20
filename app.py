import streamlit as st

# Ustawienie tytułu aplikacji
st.title("Przykładowa Strona z Nawigacją")

# Funkcja do wyświetlania treści w zależności od wybranej opcji
def show_content(selected):
    if selected == "Strona Główna":
        st.subheader("Witamy na stronie głównej!")
        st.write("To jest treść strony głównej.")
        
    elif selected == "O Nas":
        st.subheader("O Nas")
        st.write("Informacje o firmie.")
        
    elif selected == "Usługi":
        st.subheader("Nasze Usługi")
        st.write("Opis oferowanych usług.")

# Pasek nawigacyjny na całą szerokość
menu_options = ["Strona Główna", "O Nas", "Usługi"]
selected_menu = st.selectbox("Wybierz opcję:", menu_options)

# Wyświetlanie rozwijanego menu w zależności od wybranej opcji
if selected_menu == "Usługi":
    with st.expander("Rozwiń, aby zobaczyć usługi", expanded=True):
        st.write("1. Usługa A")
        st.write("2. Usługa B")
        st.write("3. Usługa C")

# Wywołanie funkcji, aby wyświetlić odpowiednią treść
show_content(selected_menu)

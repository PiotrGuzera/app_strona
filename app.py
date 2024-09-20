import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

images_path = Path("images")

# Ustawienia strony
st.set_page_config(page_title="Elegancka Strona w Streamlit", layout="wide")

# Tytuł strony
st.title("Elegancka Strona w Streamlit")

# Pasek nawigacyjny
menu_options = ["Strona Główna", "O Nas", "Usługi", "Kontakt"]
selected_menu = st.sidebar.selectbox("Wybierz opcję:", menu_options)

# Treść na podstawie wybranej opcji
if selected_menu == "Strona Główna":
    st.header("Witamy na naszej stronie!")
    st.write("To jest strona, która pokazuje, jak stworzyć elegancką aplikację w Streamlit.")
    st.image(str(images_path / "obrazek2.jpg"), caption="Siedziba", use_column_width=True)

elif selected_menu == "O Nas":
    st.header("O Nas")
    st.write("Jesteśmy firmą zajmującą się tworzeniem aplikacji webowych.")
    st.write("Naszym celem jest dostarczanie innowacyjnych rozwiązań dla naszych klientów.")
    st.image(str(images_path / "obrazek1.jpeg"), caption="Nasz zespół", use_column_width=True)

elif selected_menu == "Usługi":
    st.header("Nasze Usługi")
    services = {
        "Usługa A": "Opis Usługi A",
        "Usługa B": "Opis Usługi B",
        "Usługa C": "Opis Usługi C"
    }
    for service, description in services.items():
        st.subheader(service)
        st.write(description)
        st.image(str(images_path / "obrazek3.jpg"), caption="Usługi", use_column_width=True)

elif selected_menu == "Kontakt":
    st.header("Kontakt")
    st.write("Skontaktuj się z nami!")
    contact_form = st.form(key='contact_form')
    name = contact_form.text_input("Imię:")
    email = contact_form.text_input("Email:")
    message = contact_form.text_area("Wiadomość:")
    submit_button = contact_form.form_submit_button("Wyślij")

    if submit_button:
        st.success("Dziękujemy za wiadomość! Skontaktujemy się z Tobą wkrótce.")

# Dodanie strefy z danymi
st.sidebar.title("Statystyki")
data = pd.DataFrame({
    "Usługa": ["Usługa A", "Usługa B", "Usługa C"],
    "Liczba Klientów": [120, 80, 60],
})
st.sidebar.bar_chart(data.set_index("Usługa"))

# Przycisk do powrotu do góry
if st.sidebar.button("Powrót do góry"):
    st.experimental_rerun()

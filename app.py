import streamlit as st
import sqlite3

# Funciones para interactuar con la base de datos
def create_table():
    conn = sqlite3.connect("emoji.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emoji (id INTEGER PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()

def get_emoji():
    conn = sqlite3.connect("emoji.db")
    c = conn.cursor()
    c.execute("SELECT value FROM emoji WHERE id = 1")
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "😎"  # Emoji por defecto

def update_emoji(emoji):
    conn = sqlite3.connect("emoji.db")
    c = conn.cursor()
    c.execute("REPLACE INTO emoji (id, value) VALUES (1, ?)", (emoji,))
    conn.commit()
    conn.close()

# Crear la tabla de la base de datos si no existe
create_table()

# Obtener el emoji guardado
current_emoji = get_emoji()

# Interfaz de Streamlit
st.title("AYEMOOD")

emoji = st.text_input("Introduce un emoji:", value=current_emoji)

if st.button("ACTUALIZAR"):
    update_emoji(emoji)
    st.experimental_rerun()

st.markdown(f"<div style='text-align: center; font-size: 100px;'>{emoji}</div>", unsafe_allow_html=True)

# Ocultar la marca de agua y el menú de Streamlit
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Aplicar modo oscuro usando CSS
dark_mode_style = """
<style>
body {
    color: #FAFAFA;
    background-color: #0E1117;
}
.css-1d391kg, .css-1kyxreq, .css-1offfwp {
    background-color: #262730;
    color: #FAFAFA;
}
.st-bf, .st-bg {
    color: #FAFAFA;
}
</style>
"""
st.markdown(dark_mode_style, unsafe_allow_html=True)
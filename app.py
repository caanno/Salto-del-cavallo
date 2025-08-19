import streamlit as st
import string

# Etichette colonne A-H
cols_labels = list(string.ascii_uppercase[:8])

st.set_page_config(layout="wide")
st.markdown("## ♟️ Scacchiera Interattiva")

# CSS per rendere i bottoni grandi e leggibili anche da telefono
st.markdown("""
<style>
button[kind="secondary"] {
    width: 100% !important;
    height: 55px !important;
    font-size: 18px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Disegno scacchiera
for row in range(7, -1, -1):   # Riga 8 → 1
    cols = st.columns(8, gap="small")  # 8 colonne
    for col in range(8):  
        square_name = f"{cols_labels[col]}{row+1}"  # Es. A8, B7, ...
        color = "⬜" if (row + col) % 2 == 0 else "⬛"  # solo per indicazione logica
        with cols[col]:
            if st.button(square_name, key=square_name):
                st.session_state["selected_square"] = square_name

# Mostra casella scelta
if "selected_square" in st.session_state:
    st.success(f"Hai scelto: {st.session_state['selected_square']}")

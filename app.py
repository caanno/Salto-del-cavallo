import streamlit as st
import string

st.set_page_config(layout="wide")
cols_labels = list(string.ascii_uppercase[:8])

st.markdown("## ♟️ Scacchiera Interattiva")

for row in range(7, -1, -1):
    cols = st.columns(8)
    for col_index, col in enumerate(cols):
        square_name = f"{cols_labels[col_index]}{row+1}"
        color = "#EEE" if (row + col_index) % 2 == 0 else "#555"
        if col.button(square_name, key=square_name):
            st.write(f"Hai premuto {square_name}")
        col.markdown(f"<div style='background:{color};height:60px;width:60px'></div>", unsafe_allow_html=True)

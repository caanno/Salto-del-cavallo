import streamlit as st
import string

st.set_page_config(layout="wide")

cols_labels = list(string.ascii_uppercase[:8])

st.markdown("""
<style>
.square-btn {
    width: 60px;
    height: 60px;
    font-size: 18px;
    font-weight: bold;
    margin: 1px;
}
.row-container {
    display: flex;
}
.scroll-container {
    overflow-x: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## ♟️ Scacchiera Interattiva")

# Container scrollabile
st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

for row in range(7, -1, -1):
    cols = st.columns(8)
    for col_idx, col in enumerate(cols):
        square_name = f"{cols_labels[col_idx]}{row+1}"
        color = "#EEE" if (row + col_idx) % 2 == 0 else "#555"
        if col.button(square_name, key=square_name, help="Premi per selezionare"):
            st.write(f"Hai premuto {square_name}")
    st.markdown("---")  # separa le righe

st.markdown('</div>', unsafe_allow_html=True)

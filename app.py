import streamlit as st
import string

st.set_page_config(layout="wide")

cols_labels = list(string.ascii_uppercase[:8])

# CSS aggiornato
st.markdown("""
<style>
.board {
    display: flex;
    flex-direction: column;
    width: max-content;  /* la scacchiera resta larga quanto serve */
}
.row {
    display: flex;
    flex-wrap: nowrap;   /* impedisce che i bottoni vadano a capo */
}
.square-btn {
    width: 60px !important;
    height: 60px !important;
    font-size: 16px !important;
    font-weight: bold;
    margin: 0 !important;
    border: none;
}
.scroll-container {
    overflow-x: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## ♟️ Scacchiera Interattiva")

st.markdown('<div class="scroll-container"><div class="board">', unsafe_allow_html=True)

for row in range(7, -1, -1):  
    row_html = '<div class="row">'
    for col in range(8):  
        square_name = f"{cols_labels[col]}{row+1}"
        color = "#EEE" if (row + col) % 2 == 0 else "#555"
        row_html += f"""
        <form action="" method="get" style="display:inline;">
            <button class="square-btn" style="background:{color};color:black;" name="square" value="{square_name}">
                {square_name}
            </button>
        </form>
        """
    row_html += "</div>"
    st.markdown(row_html, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

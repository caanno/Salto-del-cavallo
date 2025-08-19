import streamlit as st
import string

st.set_page_config(layout="wide")

cols_labels = list(string.ascii_uppercase[:8])

# CSS per bottoni e container responsive
st.markdown("""
<style>
.square-btn {
    width: 8vw;  /* larghezza relativa alla viewport */
    height: 8vw;
    max-width: 60px;
    max-height: 60px;
    min-width: 30px;
    min-height: 30px;
    font-size: calc(1vw + 10px);
    font-weight: bold;
    margin: 1px !important;
}

.row-container {
    display: flex;
    justify-content: flex-start;
}
.scroll-container {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; /* scroll fluido su mobile se necessario */
}
</style>
""", unsafe_allow_html=True)

st.markdown("## ♟️ Scacchiera Interattiva")

st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

for row in range(7, -1, -1):
    row_html = '<div class="row-container">'
    for col in range(8):
        square_name = f"{cols_labels[col]}{row+1}"
        color = "#EEE" if (row + col) % 2 == 0 else "#555"
        row_html += f"""
        <form action="" method="get" style="display:inline-block;">
            <button class="square-btn" style="background:{color};color:black;" name="square" value="{square_name}">
                {square_name}
            </button>
        </form>
        """
    row_html += '</div>'
    st.markdown(row_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

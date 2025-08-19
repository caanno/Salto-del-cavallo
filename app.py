import streamlit as st
import string

st.set_page_config(layout="wide")

cols_labels = list(string.ascii_uppercase[:8])

# CSS per bottoni
st.markdown("""
<style>
.square-btn {
    width: 60px !important;
    height: 60px !important;
    font-size: 18px !important;
    font-weight: bold;
    margin: 1px !important;
}
.scroll-container {
    overflow-x: auto;
    white-space: nowrap;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## ♟️ Scacchiera Interattiva")

# Container scrollabile
st.markdown('<div class="scroll-container">', unsafe_allow_html=True)

for row in range(7, -1, -1):  
    row_html = ""
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
    st.markdown(row_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

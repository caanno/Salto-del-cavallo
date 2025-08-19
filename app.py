import streamlit as st
import string

# Config pagina
st.set_page_config(page_title="Il salto del cavallo ♞", layout="wide")

# CSS responsive per bottoni Streamlit
st.markdown("""
    <style>
    div[data-testid="stHorizontalBlock"] > div {
        flex: 1 1 12%;
        max-width: 12%;
        padding: 2px;
    }
    button[kind="secondary"] {
        aspect-ratio: 1;
        width: 100% !important;
        font-size: clamp(10px, 3vw, 20px) !important;
        font-weight: bold;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Stato
if "start_pos" not in st.session_state:
    st.session_state.start_pos = None

cols_labels = list(string.ascii_uppercase[:8])
rows_labels = list(range(8, 0, -1))

# Disegna scacchiera responsive
if st.session_state.start_pos is None:
    st.markdown("<h2 style='text-align:center;'>Scegli una casella</h2>", unsafe_allow_html=True)

    for row in rows_labels:
        cols = st.columns(8, gap="small")
        for col_idx, col in enumerate(cols):
            square_name = f"{cols_labels[col_idx]}{row}"
            with col:
                if st.button(square_name, key=square_name):
                    st.session_state.start_pos = (col_idx, row-1)
                    st.rerun()
else:
    col, row = st.session_state.start_pos
    square_name = f"{cols_labels[col]}{row+1}"
    st.markdown(f"<h3 style='text-align:center;'>Casella selezionata: {square_name}</h3>", unsafe_allow_html=True)

    if st.button("🔄 Scegli un'altra casella"):
        st.session_state.start_pos = None
        st.rerun()

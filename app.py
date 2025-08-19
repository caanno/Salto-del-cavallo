import streamlit as st
import string

# Configurazione pagina
st.set_page_config(page_title="Il salto del cavallo ♞", layout="wide")

# CSS responsive
st.markdown("""
    <style>
    .chessboard {
        display: grid;
        grid-template-columns: repeat(8, minmax(30px, 1fr));
        gap: 4px;
        max-width: 600px;
        margin: auto;
    }
    .square-btn {
        width: 100%;
        aspect-ratio: 1; /* quadrato */
        font-size: clamp(10px, 3vw, 22px);
        font-weight: bold;
        border: 1px solid #444;
        border-radius: 6px;
        cursor: pointer;
        background: white;
    }
    .square-btn:hover {
        background: #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Stato
if "start_pos" not in st.session_state:
    st.session_state.start_pos = None

cols_labels = list(string.ascii_uppercase[:8])
rows_labels = list(range(8, 0, -1))

# Disegna scacchiera
if st.session_state.start_pos is None:
    st.markdown("<h2 style='text-align:center;'>Scegli una casella</h2>", unsafe_allow_html=True)
    
    html_board = "<div class='chessboard'>"
    for row in rows_labels:
        for col_idx in range(8):
            square_name = f"{cols_labels[col_idx]}{row}"
            if st.button(square_name, key=square_name, help=f"Seleziona {square_name}"):
                st.session_state.start_pos = (col_idx, row-1)
                st.rerun()
            html_board += f"<button class='square-btn'>{square_name}</button>"
    html_board += "</div>"
    
    st.markdown(html_board, unsafe_allow_html=True)
else:
    col, row = st.session_state.start_pos
    square_name = f"{cols_labels[col]}{row+1}"
    st.markdown(f"<h3 style='text-align:center;'>Casella selezionata: {square_name}</h3>", unsafe_allow_html=True)

    if st.button("🔄 Scegli un'altra casella"):
        st.session_state.start_pos = None
        st.rerun()

import streamlit as st
import string
from knight_tour import solve_knight_tour
from animate import animate_knight_tour

def chessboard_buttons():
    cols_labels = list(string.ascii_uppercase[:8])
    rows_labels = list(range(8, 0, -1))
    selected = None
    for row in rows_labels:
        cols = st.columns(8, gap='small')
        for col_idx, col in enumerate(cols):
            square_name = f"{cols_labels[col_idx]}{row}"
            if col.button(square_name, key=square_name):
                selected = (col_idx, row-1)
    return selected

# Stato iniziale
if "start_pos" not in st.session_state:
    st.session_state.start_pos = None

# Titolo principale
st.markdown("<h1 style='text-align: center; color: brown;margin-top:-70px;'>Il salto del cavallo ♞</h1>", unsafe_allow_html=True)

# Pulsante per tornare indietro in alto a destra
if st.session_state.start_pos is not None:
    _, col_btn = st.columns([0.8, 0.2])
    with col_btn:
        if st.button("🔄 Scegli un'altra casella"):
            st.session_state.start_pos = None

if st.session_state.start_pos is None:
    st.markdown("<h2 style='text-align: center; color: gray;margin-top:-15px;font-size:18px;'>Scegli la casella da cui partire</h2>", unsafe_allow_html=True)
    pos = chessboard_buttons()
    if pos is not None:
        st.session_state.start_pos = pos
else:
    col, row = st.session_state.start_pos
    cols_labels = list(string.ascii_uppercase[:8])
    square_name = f"{cols_labels[col]}{row+1}"
    st.markdown(f"<h3 style='text-align: center; color: black;margin-top:-15px;'>Casella selezionata: {square_name}</h3>", unsafe_allow_html=True)

    with st.spinner("Calcolo del percorso del cavallo..."):
        tour = solve_knight_tour((row, col))
        if tour:
            gif_bytes = animate_knight_tour(tour, interval=500, fps=2)
            # Mostra l'animazione al posto della scacchiera
            st.image(gif_bytes, use_column_width=True)
        else:
            st.error("Nessun tour trovato")

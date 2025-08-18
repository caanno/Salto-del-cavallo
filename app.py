import streamlit as st
import string
from knight_tour import solve_knight_tour
from animate import animate_knight_tour

# Funzione per generare la griglia di bottoni
def chessboard_buttons():
    cols_labels = list(string.ascii_uppercase[:8])  # A-H
    rows_labels = list(range(8, 0, -1))  # 8-1 (origine in basso a sinistra)
    
    selected = None
    
    for row in rows_labels:
        cols = st.columns(8, gap='small')
        for col_idx, col in enumerate(cols):
            square_name = f"{cols_labels[col_idx]}{row}"
            if col.button(square_name, key=square_name):
                selected = (col_idx, row-1)  # col, row index 0-based
    return selected

# Stato iniziale
if "start_pos" not in st.session_state:
    st.session_state.start_pos = None

if st.session_state.start_pos is None:
    # Titolo e istruzioni
    st.markdown("<h1 style='text-align: center; color: brown; margin-top:-50px;'>Il salto del cavallo ♞</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: gray; margin-top:-15px; font-size:18px;'>Scegli la casella da cui partire e visualizza il percorso del cavallo sulla scacchiera</h5>", unsafe_allow_html=True)
    
    # Mostra scacchiera
    pos = chessboard_buttons()  # restituisce una coppia colonna riga corrispondente alla casella selezionata
    if pos is not None:
        st.session_state.start_pos = pos
else:
    # Pulsante per tornare indietro
    col4, col5 = st.columns([0.7,0.3])
    with col5:
        if st.button("🔄 Scegli un'altra casella"):
            st.session_state.start_pos = None    
    col, row = st.session_state.start_pos
    cols_labels = list(string.ascii_uppercase[:8])
    square_name = f"{cols_labels[col]}{row+1}"
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: brown; margin-top:-50px;'>Il salto del cavallo ♞</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: black; margin-top:-15px;'>Casella selezionata: {square_name}</h3>", unsafe_allow_html=True)

    # Calcolo tour del cavallo
    with st.spinner("Il calcolo del percorso potrebbe richiedere alcuni secondi..."):        
        tour = solve_knight_tour((row, col))
        if tour:
            gif_bytes = animate_knight_tour(tour, interval=500, fps=2)
            col1, col2, col3 = st.columns([1,4,1])
            with col2:
                st.image(gif_bytes)
        else:
            st.error('Nessun tour trovato')



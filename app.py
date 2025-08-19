import streamlit as st
import string

st.set_page_config(page_title="Il salto del cavallo ♞", layout="wide")

# Stato
if "start_pos" not in st.session_state:
    st.session_state.start_pos = None

cols_labels = list(string.ascii_uppercase[:8])
rows_labels = list(range(8, 0, -1))

# Stile scacchiera
st.markdown("""
    <style>
    .chessboard {
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        max-width: 100%;
        margin: auto;
    }
    .square-btn {
        aspect-ratio: 1 / 1;
        width: 100%;
        font-size: clamp(10px, 3vw, 22px);
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
    .white { background-color: #f0d9b5; }
    .black { background-color: #b58863; color: white; }
    .square-btn:hover {
        opacity: 0.8;
    }
    </style>
""", unsafe_allow_html=True)


# Selezione casella
if st.session_state.start_pos is None:
    st.markdown("<h2 style='text-align:center;'>Scegli una casella</h2>", unsafe_allow_html=True)

    html = '<div class="chessboard">'
    for r, row in enumerate(rows_labels):
        for c, col in enumerate(cols_labels):
            square_name = f"{col}{row}"
            color = "white" if (r+c) % 2 == 0 else "black"
            # ogni bottone manda query param "square"
            html += f"""
            <form action="" method="get">
                <input type="hidden" name="square" value="{c},{row-1}">
                <button class="square-btn {color}" type="submit">{square_name}</button>
            </form>
            """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    # Controllo se è stato cliccato un bottone
    query_params = st.query_params
    if "square" in query_params:
        col, row = map(int, query_params["square"].split(","))
        st.session_state.start_pos = (col, row)
        st.query_params.clear()   # reset query per non ricaricare sempre
        st.rerun()

else:
    col, row = st.session_state.start_pos
    square_name = f"{cols_labels[col]}{row+1}"
    st.markdown(f"<h3 style='text-align:center;'>Casella selezionata: {square_name}</h3>", unsafe_allow_html=True)

    if st.button("🔄 Scegli un'altra casella"):
        st.session_state.start_pos = None
        st.rerun()

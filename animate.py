import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.image as mpimg
from matplotlib.animation import PillowWriter
import tempfile
import os

def animate_knight_tour(
        tour,
        n=8,
        knight_icon_path="knight.png",
        save_path="knight_tour.gif",
        interval=500,
        fps=2
    ):
    # --- Crea scacchiera marrone/beige ---
    board = np.zeros((n, n, 3))
    light_color = np.array([240/255, 217/255, 181/255])  # beige
    dark_color = np.array([181/255, 136/255, 99/255])    # marrone
    for i in range(n):
        for j in range(n):
            board[i, j] = light_color if (i + j) % 2 == 0 else dark_color

    # --- Coordinate del tour ---
    xs = [pos[1] for pos in tour]
    ys = [pos[0] for pos in tour]

    # --- Setup figura ---
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(board, origin="lower")  # "upper" per avere (0,0) in alto a sinistra
    ax.set_xlim(-0.5, n-0.5)
    ax.set_ylim(-0.5, n-0.5)

    # Etichette colonne (A-H)
    ax.set_xticks(range(n))
    ax.set_xticklabels([chr(ord('A')+i) for i in range(n)], fontsize=12, fontweight='bold')
    # Etichette righe (1-8)
    ax.set_yticks(range(n))
    ax.set_yticklabels([str(i+1) for i in range(n)], fontsize=12, fontweight='bold')

    # --- Carica icona cavallo ---
    knight_img = None
    try:
        knight_img = mpimg.imread(knight_icon_path)
    except FileNotFoundError:
        print(f"⚠️ Immagine {knight_icon_path} non trovata, uso un punto.")

    # --- Oggetti aggiornabili ---
    arrows = []
    texts = []
    knight_artist = None

    def init():
        return []

    def update(frame):
        nonlocal knight_artist
        step = frame

        # Disegna freccia dalla mossa precedente a quella attuale
        if step > 0:
            arrow = ax.annotate("",
                    xy=(xs[step]-0.1, ys[step]-0.1),  # punta leggermente spostata
                    xytext=(xs[step-1], ys[step-1]),
            arrowprops=dict(
                arrowstyle="-|>,head_width=0.5,head_length=0.7",
                color="red", lw=2.5),
    zorder=2
)

            arrows.append(arrow)

        # Aggiungi numero della mossa
        txt = ax.text(xs[step], ys[step], str(step+1),
                      color="blue", fontsize=10, ha='center', va='center', fontweight='bold',
                      bbox=dict(facecolor="white", edgecolor="black", boxstyle="circle,pad=0.3"))
        texts.append(txt)

        # Aggiorna cavallo
        if knight_img is not None:
            if knight_artist:
                knight_artist.remove()
            knight_artist = ax.imshow(knight_img,
                                      extent=(xs[step]-0.5, xs[step]+0.5, ys[step]-0.5, ys[step]+0.5),
                                      zorder=15)
        return arrows + texts + ([knight_artist] if knight_img is not None else [])

    ani = animation.FuncAnimation(fig, update, frames=len(tour),
                                  init_func=init, blit=True, repeat=False, interval=interval)

    '''ani.save(save_path, writer="pillow", fps=fps) #salva la gif
    print(f"✅ Animazione salvata in {save_path}")
    plt.close(fig)'''

    tmp_path = tempfile.mktemp(suffix=".gif")  # solo path, non aperto
    ani.save(tmp_path, writer=PillowWriter(fps=fps))
    
    with open(tmp_path, "rb") as f:
        gif_bytes = f.read()
    
    os.remove(tmp_path)
    plt.close(fig)
    return gif_bytes

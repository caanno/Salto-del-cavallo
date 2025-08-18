import random

def knight_moves(i, j, n):
    """
    Restituisce tutte le mosse legali del cavallo dalla casella (i,j) su scacchiera n x n.
    """
    steps = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    return [(i+di, j+dj) for di, dj in steps if 0 <= i+di < n and 0 <= j+dj < n]

def solve_knight_tour(start_pos, n=8):
    """
    Trova un percorso del cavallo partendo da start_pos = (riga, colonna).
    Usa Warnsdorff + randomizzazione per avere tour diversi.
    Restituisce una lista di posizioni [(i,j), ...] oppure None se non trovato.
    """
    board = [[-1 for _ in range(n)] for _ in range(n)]
    path = [start_pos]
    board[start_pos[0]][start_pos[1]] = 0  # casella di partenza

    def warnsdorff_degree(cell):
        """Numero di mosse disponibili dalla cella."""
        return sum(1 for m in knight_moves(*cell, n) if board[m[0]][m[1]] == -1)

    def backtrack(step, pos):
        if step == n * n:
            return True

        moves = [(m, warnsdorff_degree(m)) for m in knight_moves(*pos, n) if board[m[0]][m[1]] == -1]

        # ordina per grado, ma randomizza tra mosse con stesso grado
        moves.sort(key=lambda x: x[1])
        grouped = []
        i = 0
        while i < len(moves):
            j = i
            while j < len(moves) and moves[j][1] == moves[i][1]:
                j += 1
            group = moves[i:j]
            random.shuffle(group)
            grouped.extend(group)
            i = j
        moves = grouped

        for move, _ in moves:
            board[move[0]][move[1]] = step
            path.append(move)
            if backtrack(step + 1, move):
                return True
            # backtrack
            board[move[0]][move[1]] = -1
            path.pop()

        return False

    if backtrack(1, start_pos):
        return path
    else:
        return None


'''# Test rapido
if __name__ == "__main__":
    start = (0, 0)
    for k in range(3):
        tour = solve_knight_tour(start)
        print(f"\nTour {k+1}:")
        if tour:
            print(tour[:10], "...")  # stampo solo le prime 10 mosse per brevità
        else:
            print("Nessun tour trovato")'''

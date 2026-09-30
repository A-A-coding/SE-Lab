# check_parity.py
from puzzle import Puzzle

def solvable(board, n):
    flat = [x for row in board for x in row]
    tiles = [x for x in flat if x]
    inv = sum(1 for i in range(len(tiles))
              for j in range(i + 1, len(tiles)) if tiles[i] > tiles[j])
    if n % 2 == 1:
        return inv % 2 == 0
    blank_row_from_bottom = n - flat.index(0) // n
    return (inv + blank_row_from_bottom) % 2 == 1

for n in (3, 4, 5):
    bad = already_solved = 0
    for _ in range(1000):
        p = Puzzle(n)
        if not solvable(p.board, n):
            bad += 1
        if p.solved():
            already_solved += 1
    print(f"{n}x{n}: unsolvable={bad}/1000, started solved={already_solved}/1000")
import random

SIZES = (3, 4, 5)
DIRECTIONS = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
OPPOSITE = {"w": "s", "s": "w", "a": "d", "d": "a"}


class Puzzle:
    def __init__(self, size=4):
        if size not in SIZES:
            raise ValueError(f"size must be one of {SIZES}")
        self.size = size
        self.board = self.make_board()

    def move(self, direction):
        """Return the tile that slid into the blank, or None if nothing moved."""
        if self.solved() or direction not in DIRECTIONS:
            return None
        return self._slide(direction)

    def solved_board(self):
        n = self.size
        tiles = list(range(1, n * n)) + [0]
        return [tiles[r * n:(r + 1) * n] for r in range(n)]

    def make_board(self):
        # Scramble with legal moves only, so the result is always solvable.
        while True:
            self.board = self.solved_board()
            last = None
            for _ in range(self.size * self.size * 20):
                options = [d for d in DIRECTIONS
                           if d != OPPOSITE.get(last) and self._can_slide(d)]
                last = random.choice(options)
                self._slide(last)
            if not self.solved():
                return self.board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def _target(self, direction):
        r, c = self.blank_pos()
        dr, dc = DIRECTIONS[direction]
        return r, c, r + dr, c + dc

    def _can_slide(self, direction):
        _, _, nr, nc = self._target(direction)
        return 0 <= nr < self.size and 0 <= nc < self.size

    def _slide(self, direction):
        if not self._can_slide(direction):
            return None
        r, c, nr, nc = self._target(direction)
        tile = self.board[nr][nc]
        self.board[r][c], self.board[nr][nc] = tile, 0
        return tile

    def solved(self):
        return self.board == self.solved_board()
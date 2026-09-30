import time
from puzzle import Puzzle, SIZES


class SlidingPuzzle:
    def __init__(self):
        self.size = 4
        self.puzzle = None
        self.moves = 0
        self.started = None
        self.finished_at = None

    def new_board(self):                 # board only; session values untouched
        self.puzzle = Puzzle(self.size)

    def start_session(self, size):       # the only place counters are reset
        self.size = size
        self.new_board()
        self.moves = 0
        self.started = time.monotonic()
        self.finished_at = None

    def elapsed(self):
        end = self.finished_at if self.finished_at is not None else time.monotonic()
        return int(end - self.started)

    def choose_size(self):
        while True:
            raw = input(f"Board size {SIZES}: ").strip()
            if raw.isdigit() and int(raw) in SIZES:
                return int(raw)
            print("Please enter 3, 4 or 5.")

    def display(self):
        width = len(str(self.size * self.size - 1))
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or '':>{width}}" for x in row))
        print("Moves:", self.moves, " Time:", self.elapsed(), "s")

    def run(self):
        print("Sliding Puzzle — W/A/S/D moves the tile into the blank. Q quits.")
        self.start_session(self.choose_size())
        while True:
            self.display()
            if self.puzzle.solved():
                print(f"Solved in {self.moves} moves and {self.elapsed()}s!")
                return
            key = input("> ").strip().lower()
            if key == "q":
                return
            if key not in ("w", "a", "s", "d"):
                print("Use W/A/S/D (or Q to quit).")
                continue
            tile = self.puzzle.move(key)
            if tile is None:
                print("That move is not possible.")
            else:
                self.moves += 1
                print(f"Slid tile {tile}.")
                if self.puzzle.solved():
                    self.finished_at = time.monotonic()   # freeze the timer
import unittest
from puzzle import Puzzle


class Task4Tests(unittest.TestCase):
    def setUp(self):
        self.p = Puzzle(3)
        self.p.board = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]   # blank bottom-right, not solved

    def test_valid_move_returns_tile(self):
        self.assertEqual(self.p.move("a"), 7)     # 7 slides right into the blank
        self.assertEqual(self.p.board[2], [8, 0, 7])

    def test_wall_moves_return_none_and_change_nothing(self):
        before = [row[:] for row in self.p.board]
        self.assertIsNone(self.p.move("s"))       # wall below
        self.assertIsNone(self.p.move("d"))       # wall right
        self.assertEqual(self.p.board, before)

    def test_invalid_keys_return_none(self):
        before = [row[:] for row in self.p.board]
        for bad in ("", "x", "wa", "12"):
            self.assertIsNone(self.p.move(bad))
        self.assertEqual(self.p.board, before)


if __name__ == "__main__":
    unittest.main()
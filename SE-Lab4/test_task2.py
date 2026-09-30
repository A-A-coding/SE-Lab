import time
import unittest
from game import SlidingPuzzle
from puzzle import Puzzle


class Task2Tests(unittest.TestCase):
    def make_near_solved(self):
        p = Puzzle(3)
        p.board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]   # one move from solved
        return p

    def test_winning_move_solves(self):
        p = self.make_near_solved()
        self.assertTrue(p.move("d"))
        self.assertTrue(p.solved())

    def test_board_locked_after_solve(self):
        p = self.make_near_solved()
        p.move("d")
        before = [row[:] for row in p.board]
        for key in "wasd":
            self.assertFalse(p.move(key))
        self.assertEqual(p.board, before)

    def test_timer_freezes(self):
        g = SlidingPuzzle()
        g.finished_at = g.started + 7
        self.assertEqual(g.elapsed(), 7)
        time.sleep(1.1)
        self.assertEqual(g.elapsed(), 7)


if __name__ == "__main__":
    unittest.main()
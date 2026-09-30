import unittest
from game import SlidingPuzzle
from puzzle import Puzzle


class Task3Tests(unittest.TestCase):
    def test_all_sizes_build_correct_boards(self):
        for n in (3, 4, 5):
            p = Puzzle(n)
            self.assertEqual(len(p.board), n)
            self.assertTrue(all(len(row) == n for row in p.board))
            flat = sorted(x for row in p.board for x in row)
            self.assertEqual(flat, list(range(n * n)))

    def test_unsupported_sizes_rejected(self):
        for bad in (2, 6, 0, -1):
            with self.assertRaises(ValueError):
                Puzzle(bad)

    def test_new_board_keeps_session_values(self):
        g = SlidingPuzzle()
        g.start_session(3)
        g.moves = 5
        started = g.started
        g.new_board()
        self.assertEqual(g.moves, 5)
        self.assertEqual(g.started, started)

    def test_start_session_resets_and_sets_size(self):
        g = SlidingPuzzle()
        g.start_session(3)
        g.moves = 9
        g.finished_at = g.started + 1
        g.start_session(5)
        self.assertEqual(g.size, 5)
        self.assertEqual(len(g.puzzle.board), 5)
        self.assertEqual(g.moves, 0)
        self.assertIsNone(g.finished_at)

    def test_timer_runs_for_every_size(self):
        for n in (3, 4, 5):
            g = SlidingPuzzle()
            g.start_session(n)
            self.assertGreaterEqual(g.elapsed(), 0)


if __name__ == "__main__":
    unittest.main()
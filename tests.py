import unittest
from maze import Maze

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertEqual(
      len(m1._cells),
      num_cols,
    )
    self.assertEqual(
      len(m1._cells[0]),
      num_rows,
    )
    m2 = Maze(10, 10, 20, 20, 10, 10)
    self.assertEqual(
      len(m2._cells),
      20
    )
    self.assertEqual(
      len(m2._cells[0]),
      20,
    )

  def test_maze_entrance_exit(self):
    m3 = Maze(0, 0, 10, 10, 10, 10)
    self.assertEqual(
      m3._cells[0][0].has_top_wall,
      False
    )
    self.assertEqual(
      m3._cells[0][1].has_top_wall,
      True
    )
    self.assertEqual(
      m3._cells[9][9].has_bottom_wall,
      False
    )

  def test_maze_reset_cells_visted(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    for col in m1._cells:
      for cell in col:
        self.assertEqual(
          cell.visited,
          False,
        )

if __name__ == "__main__":
  unittest.main()
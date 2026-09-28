import unittest
from calculator import calculate_percentage, get_defaulters
from validator import check_valid_rolls


class TestTracker(unittest.TestCase):

  def test_percentage_calculation(self):
    self.assertEqual(calculate_percentage([1, 1, 1, 1, 0]), 80.0)

  def test_threshold_boundary(self):
    records = {
        "A": [1] * 749 + [0] * 251,  # 74.9% -> defaulter
        "B": [1, 1, 1, 0],  # 75.0% -> still eligible
    }
    self.assertEqual(get_defaulters(records), ["A"])

  def test_invalid_roll_detection(self):
    enrolled = {"101", "102", "103", "104"}
    valid, invalid = check_valid_rolls("101 999 101 103", enrolled)
    self.assertEqual(valid, ["101", "103"])
    self.assertEqual(invalid, ["999"])


if __name__ == "__main__":
  unittest.main()
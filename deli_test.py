import sys
import unittest

from deli import line, take_a_number, now_serving

class TestDeli(unittest.TestCase):


    def test_line(self):
        """It shows every value in a list and returns 'The line is currently empty.' if given an empty list'""
        self.assertEqual(line([]), The line is currently empty.')

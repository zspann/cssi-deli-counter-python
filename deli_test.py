import sys
import unittest

from deli import line, take_a_number, now_serving

empty_deli=[]
full_deli=["Nicki", "Danny", "Rob"]
other_empty_deli=[]
other_full_deli=["Larry", "Curly", "Moe"]

class TestLine(unittest.TestCase):

    def test_line_empty(self):
        self.assertEqual(line(empty_deli), 'The line is currently empty.')

    def test_line(self):
        self.assertEqual(line(full_deli), 'The line is currently: 1. Nicki 2. Danny 3. Rob')

class TestTakeNumber(unittest.TestCase):
    def test_take_a_number_empty(self):
        self.assertEqual(take_a_number(empty_deli, "Steve"), "Welcome, Steve. You are number 1 in line.")
        self.assertEqual(empty_deli,["Steve"])

    def test_take_a_number(self):
        self.assertEqual(take_a_number(full_deli, "Grace"), "Welcome, Grace. You are number 4 in line.")
        self.assertEqual(full_deli, ["Nicki","Danny", "Rob", "Grace"])

    def test_adding_multiple_ppl(self):
        take_a_number(other_empty_deli, "Ada")
        take_a_number(other_empty_deli, "Grace")
        take_a_number(other_empty_deli, "Kent")
        self.assertEqual(other_empty_deli,["Ada", "Grace", "Kent"])

class TestNowServing(unittest.TestCase):
    def test_now_serving_empty(self):
        self.assertEqual(now_serving(empty_deli),"There is nobody waiting to be served!")
    def test_now_serving(self):
        self.assertEqual(now_serving(other_full_deli), "Currently serving Larry.")
        self.assertEqual(other_full_deli, ["Curly", "Moe"])

if __name__ == '__main__':
    unittest.main()

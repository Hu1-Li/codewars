# coding=utf-8
import unittest
from solutions.parse_int import parse_int


class MostFreqWordsTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse_int("one"), 1)
        self.assertEqual(parse_int("twenty"), 20)
        self.assertEqual(parse_int("two hundred forty-six"), 246)
        self.assertEqual(parse_int("twenty hundred forty-six"), 2046)
        self.assertEqual(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"), 783919)

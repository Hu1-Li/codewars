# coding=utf-8
import unittest
from solutions.screen_locking_pattern import count_patterns_from, generate_pattern


class ScreenLockingPatternTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_patterns_from("A", 10), 0)
        self.assertEqual(count_patterns_from("A", 0), 0)
        self.assertEqual(count_patterns_from("E", 14), 0)
        self.assertEqual(count_patterns_from("B", 1), 1)
        self.assertEqual(count_patterns_from("C", 2), 5)
        self.assertEqual(count_patterns_from("E", 2), 8)
        self.assertEqual(count_patterns_from("E", 4), 256)

    def test_gen(self):
        generate_pattern()

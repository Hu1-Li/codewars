# coding=utf-8
import unittest
from solutions.evaluate_expression import calc


class EvaluateExpressionTestCase(unittest.TestCase):
    def test_simple(self):
        cases = (
            ("1 + 2 * 3", 7),
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("(1 + 2) * 3", 9),
            ("(1 + 2 + 3) * ( 4 - 2 )", 12),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10 + 1 * 10 / 2", 15),
            ("10- 2- -5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14),
            ("36 + -95 - -66 - 38 - 8 / -37 / -6 - 75", -106.036036036),
            ("-77 + -57 - -61 / -54 / -49 - -67 / 94 - 22", -155.26418037664237)
        )

        for x, y in cases:
            self.assertAlmostEqual(calc(x), y, delta=1e-6)

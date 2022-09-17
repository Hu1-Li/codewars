# coding=utf-8
import unittest
from solutions.huffman_encoding import encode, decode, frequencies


class HuffmanTestCase(unittest.TestCase):
    def test_encode(self):
        s = "aaaabcc"
        freqs = frequencies(s)
        self.assertEqual(encode(freqs, s), "0000111010")

    def test_decode(self):
        s = "aaaabcc"
        freqs = frequencies(s)
        self.assertEqual(
            decode(freqs, "0000111010"),
            s,
        )

    def test_encode_decode(self):
        s = "abcaabbccabc"
        freqs = frequencies(s)
        self.assertEqual(
            decode(freqs, encode(freqs, s)),
            s,
        )

    def test_freq(self):
        s = "aaaabcc"
        fs = frequencies(s)
        self.assertEqual(sorted(fs), [("a", 4), ("b", 1), ("c", 2)])

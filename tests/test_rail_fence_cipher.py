# coding=utf-8
# coding=utf-8
import unittest
from solutions.rail_fence_cipher import decode_rail_fence_cipher, encode_rail_fence_cipher, Encoder, Decoder


class RailFenceCipher(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN")
        self.assertEqual(encode_rail_fence_cipher("Hello, World!", 3), "Hoo!el,Wrdl l")
        self.assertEqual(encode_rail_fence_cipher("Hello, World!", 4), "H !e,Wdloollr")
        self.assertEqual(encode_rail_fence_cipher("", 3), "")

    def test_decode(self):
        self.assertEqual(decode_rail_fence_cipher("H !e,Wdloollr", 4), "Hello, World!")
        self.assertEqual(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3), "WEAREDISCOVEREDFLEEATONCE")
        self.assertEqual(decode_rail_fence_cipher("", 3), "")
        self.assertEqual(decode_rail_fence_cipher("123456789", 5), "135798642")
        self.assertEqual(decode_rail_fence_cipher("12345678", 5), "12468753")

    def test_encode_decode(self):
        string = "WEAREDISCOVEREDFLEEATONCE"

        for n in range(2, 15):
            self.assertEqual(
                decode_rail_fence_cipher(
                    encode_rail_fence_cipher(string, n),
                    n,
                ),
                string,
            )

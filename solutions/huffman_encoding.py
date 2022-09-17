# coding=utf-8
import heapq
from collections import Counter
from typing import Optional


# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    return Counter(s).items()


class Node(object):
    def __init__(
        self,
        left: Optional["Node"],
        right: Optional["Node"],
        value: Optional[str],
        freq: int,
    ):
        self.left = left
        self.right = right
        self.value = value
        self.freq = freq

    def __lt__(self, other: "Node"):
        return self.freq < other.freq

    def __gt__(self, other: "Node"):
        return self.freq > other.freq


class HuffmanTree(object):
    def __init__(self, freqs: list):
        self.tree = self.generate_tree(freqs)

    def generate_tree(self, freqs: list):
        freqs = sorted(freqs, key=lambda i: i[1], reverse=True)
        heap: list[Node] = []
        for c, freq in freqs:
            heapq.heappush(
                heap,
                Node(
                    left=None,
                    right=None,
                    value=c,
                    freq=freq,
                ),
            )

        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            heapq.heappush(
                heap,
                Node(
                    left=node2,
                    right=node1,
                    value="",
                    freq=node1.freq + node2.freq,
                ),
            )

        return heapq.heappop(heap)

    def get_mapping(self):
        """
        return mapping of value with its binary string
        """
        table = {}

        def dfs(_tree: Node, _str: str = ""):
            if _tree.left:
                dfs(_tree.left, _str + "0")

            if _tree.right:
                dfs(_tree.right, _str + "1")

            # update mapping
            if _tree.value:
                table[_tree.value] = _str

        dfs(self.tree)
        return table

    def encode(self, s: str) -> str:
        table = self.get_mapping()
        return "".join([table.get(c) for c in s])

    def decode(self, bits: str) -> str:
        table = self.get_mapping()
        rtable = {v: k for k, v in table.items()}
        s = ""
        tmp = ""
        for c in bits:
            tmp += c
            if tmp in rtable:
                s += rtable.get(tmp)
                tmp = ""
        return s


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs: list, s: str):
    if len(freqs) <= 1:
        return None

    huffman_tree = HuffmanTree(freqs)
    return huffman_tree.encode(s)


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs: list, bits: str):
    if len(freqs) <= 1:
        return None

    huffman_tree = HuffmanTree(freqs)
    return huffman_tree.decode(bits)

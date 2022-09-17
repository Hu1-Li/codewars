# coding=utf-8


class Node(object):
    def __init__(self, value: str, level: int):
        self.value = value
        self.level = level


class Encoder(object):
    def __init__(self, string: str, n: int):
        self.string = string
        self.n = n
        self.tree = self.generate_tree()

    def generate_tree(self):
        nodes = []
        m = 2 * (self.n - 1)
        for index, c in enumerate(self.string):
            level = index % m
            if level >= self.n:
                # bottom up
                level = m - level

            node = Node(
                value=c,
                level=level,
            )
            nodes.append(node)
        return nodes

    def get_level_nodes(self):
        level_nodes = []

        for _ in range(self.n):
            level_nodes.append([])

        for node in self.tree:
            level_nodes[node.level].append(node)

        return level_nodes

    @property
    def get_encoded_str(self):
        if self.n == 1:
            return self.string
        # output by level
        return "".join(["".join([node.value for node in level_node]) for level_node in self.get_level_nodes()])


class Decoder(object):
    def __init__(self, string: str, n: int):
        self.string = string
        self.n = n
        self.tree = self.generate_tree()

    def generate_tree(self):
        """
        case1: string=1243, n=3 => [1,2,3,4]

            1
              2   4
                3

        case2: string=15243, n=3 => [1,2,3,4,5]

            1       5
              2   4
                3

        case3: string=152463, n=3 => [1,2,3,4,5,6]


            1       5
              2   4   6
                3

        case3: string=1524637, n=3 => [1,2,3,4,5,6,7]


            1       5
              2   4   6
                3      7

        len(string) % (2 * (n-1))
        0 => case1
        1 => case2
        2 => case3
        3 => case4
        """
        level_nodes = []
        m = 2 * (self.n - 1)
        _div, _mod = divmod(len(self.string), m)
        level_len = [0] * self.n

        for _level, _len in enumerate(level_len):
            # div
            div_len = (1 if _level % self.n == 0 else 2) * _div
            # mod
            if _mod >= 2 * self.n - 1 - _level:
                if _level % self.n == 0:
                    mod_len = 1
                else:
                    mod_len = 2
            else:
                if _mod > _level:
                    mod_len = 1
                else:
                    mod_len = 0

            level_len[_level] += div_len + mod_len

        _index = 0
        for _level, _len in enumerate(level_len):
            nodes = [Node(value=_c, level=_level) for _c in self.string[_index : _index + _len]]
            level_nodes.append(nodes)
            _index += _len
        return level_nodes

    @property
    def get_decoded_str(self):
        if self.n == 1:
            return self.string
        # output by index
        nodes = []
        index = [0] * len(self.tree)
        m = 2 * (self.n - 1)
        for _index in range(len(self.string)):
            level = _index % m
            if level >= self.n:
                # bottom up
                level = m - level
            node = self.tree[level][index[level]]
            nodes.append(node.value)
            index[level] += 1
        return "".join(nodes)


def encode_rail_fence_cipher(string: str, n: int):
    return Encoder(string, n).get_encoded_str


def decode_rail_fence_cipher(string: str, n: int):
    return Decoder(string, n).get_decoded_str

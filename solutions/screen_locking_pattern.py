# coding=utf-8
from itertools import permutations


def count_patterns_from(firstPoint: str, length: int):
    # Your code here!
    if length <= 0 or length >= 10:
        return 0

    # ACGI
    if firstPoint in {"A", "C", "G", "I"}:
        firstPoint = "A"

    # BDHF
    if firstPoint in {"B", "D", "H", "F"}:
        firstPoint = "B"

    # E

    key = (firstPoint, length)

    mp = {
        # A
        ("A", 1): 1,
        ("A", 2): 5,
        ("A", 3): 31,
        ("A", 4): 154,
        ("A", 5): 684,
        ("A", 6): 2516,
        ("A", 7): 7104,
        ("A", 8): 13792,
        ("A", 9): 13792,
        # B
        ("B", 1): 1,
        ("B", 2): 7,
        ("B", 3): 37,
        ("B", 4): 188,
        ("B", 5): 816,
        ("B", 6): 2926,
        ("B", 7): 8118,
        ("B", 8): 15564,
        ("B", 9): 15564,
        # E
        ("E", 1): 1,
        ("E", 2): 8,
        ("E", 3): 48,
        ("E", 4): 256,
        ("E", 5): 1152,
        ("E", 6): 4248,
        ("E", 7): 12024,
        ("E", 8): 23280,
        ("E", 9): 23280,
    }
    return mp.get(key)


def generate_pattern():
    start_points = ["A", "B", "E"]
    points = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    n = 9

    rules = {
        "AC": "B",
        "DF": "E",
        "GI": "H",
        "AG": "D",
        "BH": "E",
        "CI": "F",
        "AI": "E",
        "GC": "E",
    }
    rrules = {}
    for _pattern, _point in rules.items():
        rrules["".join(list(reversed(_pattern)))] = _point

    rules.update(rrules)

    def is_valid_pattern(_previous_pattern: str, _pattern: str) -> bool:
        _previous_pattern_point = set(_previous_pattern)
        _key = _previous_pattern[-1] + _pattern
        _check_point = rules.get(_key, None)
        if _check_point and _check_point not in _previous_pattern_point:
            return False
        return True

    def get_pattern(p: str, i: int, previous: list) -> list:
        if i == 1:
            return [p]

        current = []

        # permute all the patterns, do filter
        for _previous_pattern in previous:
            _points = list(set(points) - set(_previous_pattern))
            for _pattern in permutations(_points, i - len(previous[0])):
                _pattern = "".join(_pattern)
                if is_valid_pattern(_previous_pattern, _pattern):
                    current.append(_previous_pattern + _pattern)
        return current

    mp = {}

    for p in start_points:
        _pattern = []
        for i in range(1, n + 1):
            _pattern = get_pattern(p, i, _pattern)
            mp[(p, i)] = len(_pattern)

    # copy the mp to previous function
    print(mp)

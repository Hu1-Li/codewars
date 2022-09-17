# coding=utf-8


def interpreter(code: str, iterations: int, width: int, height: int):
    def get_jump_table_from_stack(_stack: list) -> dict:
        __stack = []
        _table = {}
        for _op, _index in _stack:
            if _op == "[":
                __stack.append((_op, _index))
            else:
                __op, __index = __stack.pop()
                _table[_index] = __index
                _table[__index] = _index
        return _table

    def get_jump_table(_code: str) -> dict:
        table = {}
        stack = []
        balance = 0
        for _index, _op in enumerate(_code):
            if _op == "[" or _op == "]":
                stack.append((_op, _index))
                balance += 1 if _op == "[" else -1
                if balance == 0:
                    # gen table
                    table.update(get_jump_table_from_stack(stack))
                    stack[:] = []
            else:
                continue

        # stack not empty
        while len(stack) > 0:
            _op, _index = tuple(stack.pop())
            # no jump, break the execution
            table[_index] = -1
        return table

    jump_table = get_jump_table(code)

    registers = []
    for _ in range(height):
        registers.append([0 for _ in range(width)])

    def output():
        return "\r\n".join(["".join(map(str, line)) for line in registers])

    def flip(_hidx, _widx):
        registers[_hidx][_widx] ^= 1

    hindex, windex = 0, 0
    code_index = 0
    iter_count = 0

    while True:
        hindex = hindex % height
        windex = windex % width
        if not (0 <= code_index < len(code) and iter_count < iterations):
            break

        if not (0 <= hindex < height and 0 <= windex < width):
            break

        op = code[code_index]
        if op == "n":
            hindex -= 1
            code_index += 1
            iter_count += 1
        elif op == "e":
            windex += 1
            code_index += 1
            iter_count += 1
        elif op == "s":
            hindex += 1
            code_index += 1
            iter_count += 1
        elif op == "w":
            windex -= 1
            code_index += 1
            iter_count += 1
        elif op == "*":
            flip(hindex, windex)
            code_index += 1
            iter_count += 1
        elif op == "[":
            code_index = jump_table[code_index] + 1 if registers[hindex][windex] == 0 else code_index + 1
            iter_count += 1
        elif op == "]":
            code_index = jump_table[code_index] + 1 if registers[hindex][windex] != 0 else code_index + 1
            iter_count += 1
        else:
            code_index += 1
    return output()

# coding=utf-8
def boolfuck(code: str, input: str = "") -> str:
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

    # left padding 0
    input_bits = "".join([bin(ord(c))[2:][::-1].ljust(8, "0") for c in input])

    def _get_bit():
        for bit in input_bits:
            yield int(bit)

    get_bit = _get_bit()

    registers = [0]
    code_index = 0
    register_index = 0
    result = ""

    def flip(_idx):
        registers[_idx] ^= 1

    def output(s: str) -> str:
        _div, _mod = divmod(len(s), 8)
        _range = _div + (1 if _mod > 0 else 0)
        return "".join([chr(int(s[_i * 8 : (_i + 1) * 8][::-1].rjust(8, "0"), 2)) for _i in range(_range)])

    while True:
        if not (0 <= code_index < len(code)):
            break

        op = code[code_index]

        if op == "+":
            flip(register_index)
            code_index += 1
        elif op == ",":
            registers[register_index] = next(get_bit, 0)
            code_index += 1
        elif op == ";":
            result += str(registers[register_index])
            code_index += 1
        elif op == "<":
            if register_index == 0:
                registers.insert(register_index, 0)
            else:
                register_index -= 1
            code_index += 1
        elif op == ">":
            if register_index == len(registers) - 1:
                register_index += 1
                registers.insert(register_index, 0)
            else:
                register_index += 1
            code_index += 1
        elif op == "[":
            code_index = jump_table[code_index] + 1 if registers[register_index] == 0 else code_index + 1
        elif op == "]":
            code_index = jump_table[code_index] if registers[register_index] != 0 else code_index + 1
        else:
            code_index += 1

    return output(result)

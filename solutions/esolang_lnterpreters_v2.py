# coding=utf-8
def interpreter(code: str, tape: str) -> str:
    # Implement your interpreter here
    registers = [c for c in tape]
    zero = "0"
    one = "1"

    def flip(_index: int):
        registers[_index] = one if registers[_index] == zero else zero

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

    code_index = 0
    register_index = 0

    jump_table = get_jump_table(code)

    while True:
        if register_index < 0 or register_index >= len(registers):
            break

        if code_index < 0 or code_index >= len(code):
            break

        op = code[code_index]

        if op == ">":
            register_index += 1
            code_index += 1
        elif op == "<":
            register_index -= 1
            code_index += 1
        elif op == "*":
            flip(register_index)
            code_index += 1
        elif op == "[":
            code_index = jump_table[code_index] if registers[register_index] == zero else code_index + 1
        elif op == "]":
            code_index = jump_table[code_index] if registers[register_index] != zero else code_index + 1
        else:
            code_index += 1
    return "".join(registers)

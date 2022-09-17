# coding=utf-8
def my_first_interpreter(code: str):
    # Make your esolang interpreter here
    register = 0
    output = ""
    for op in code:
        if op == "+":
            register = (register + 1) % 256

        if op == ".":
            output += chr(register)

    return output

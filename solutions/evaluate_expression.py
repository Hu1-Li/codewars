# coding=utf-8
import re

def calc(expression: str) -> float:
    # op: "+", "-"
    # op: "*", "/"
    # op: "-"
    # op: "(", ")"
    preceeding = {
        "+": -10,
        "-": -10,
        "*": 10,
        "/": 10,
        "(": -20,
        ")": 20,
    }

    def replace_op(m):
        return f" {m.group(0)} "

    def convert_number(num: str):
        try:
            return int(num)
        except ValueError:
            return float(num)

    exprs = []
    for _expr in re.sub(r"([\+\-\*\/\(\)])", replace_op, expression).split():
        if _expr in preceeding:
            exprs.append(_expr)
        else:
            exprs.append(convert_number(_expr))

    def evaluate_expr(
        left,
        op: str,
        right,
    ):
        if op == "+":
            return left + right
        elif op == "-":
            return left - right
        elif op == "*":
            return left * right
        elif op == "/":
            return left / right
        else:
            # bad op, only support +-*/
            raise

    def is_op(_expr) -> bool:
        return _expr in preceeding

    def evaluate(_exprs: list):
        stack = []

        def stack_match_bracket(op: str = "("):
            _stack_exprs = []
            while stack:
                _expr = stack.pop()
                if _expr == op:
                    return _stack_exprs[::-1]
                else:
                    _stack_exprs.append(_expr)
            # bad expr, no matching ()
            return None

        for _index, _expr in enumerate(_exprs):
            if is_op(_expr):
                # op
                if _expr == ")":
                    # pop until "(", then evaluate
                    stack.append(evaluate(stack_match_bracket()))
                else:
                    stack.append(_expr)
            else:
                # look back: for '-'
                if 1 <= _index <= len(_exprs) - 1 and stack:
                    # back 1: -15
                    # back 2: + -15
                    minus_count = 0
                    for _stack_expr in list(stack[::-1]):
                        if is_op(_stack_expr) and _stack_expr == "-":
                            minus_count += 1
                            stack.pop()
                        else:
                            break
                    if minus_count > 0:
                        if stack and not is_op(stack[-1]):
                            # convert 2 + --3 => 2 + 3
                            # convert 2 + -3  => 2 + (-3)
                            # convert --3     => 3
                            stack.append("+")
                        _expr = (1 if (minus_count % 2 == 0) else -1) * _expr

                # look ahead
                if _index >= len(_exprs) - 1:
                    # no look ahead, end of expr
                    if not stack:
                        stack.append(_expr)
                    else:
                        _op = stack.pop()
                        _left = stack.pop()
                        stack.append(
                            evaluate_expr(
                                left=_left,
                                op=_op,
                                right=_expr,
                            )
                        )
                else:
                    if stack:
                        _next_expr = _exprs[_index + 1]
                        _stack_expr = stack.pop()
                        if preceeding.get(_stack_expr) >= preceeding.get(_next_expr):
                            _left = stack.pop()
                            stack.append(
                                evaluate_expr(
                                    left=_left,
                                    op=_stack_expr,
                                    right=_expr,
                                )
                            )
                        else:
                            stack.append(_stack_expr)
                            stack.append(_expr)
                    else:
                        stack.append(_expr)

        if len(stack) == 1:
            return stack[0]
        else:
            return evaluate(stack)

    return evaluate(exprs)

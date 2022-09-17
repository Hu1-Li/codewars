# coding=utf-8
def solution(args: list[int]) -> str:
    diffs = [args[i] - args[i - 1] for i in range(1, len(args))]
    outputs = []
    index = 0

    def find_consecutive(start_index):
        max_index = 0
        for index in range(start_index, len(diffs)):
            if diffs[index] == 1:
                max_index = index
                continue
            else:
                return max_index
        return max(max_index, start_index)

    while index <= len(diffs):
        if index == len(diffs):
            outputs.append(f"{args[index]}")
            break

        diff = diffs[index]
        if diff > 1:
            outputs.append(f"{args[index]}")
            index += 1
        else:
            max_index = find_consecutive(index)
            if max_index - index >= 1:
                # consecutive
                outputs.append(f"{args[index]}-{args[max_index + 1]}")
                index = max_index + 2
            else:
                for _index in range(index, max_index + 1):
                    outputs.append(f"{args[_index]}")
                index = max_index + 1

    return ",".join(outputs)

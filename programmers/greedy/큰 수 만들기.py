# time out error로 풀리지 않음.
def solution(number, k):

    num_origin = number
    total_len = len_need = len(number) - k

    value = ""

    idx = number.index(max(number))

    while len_need:
        if len(number[idx:]) >= len_need:
            value += number[idx]
            len_need -= 1
            number = number[idx + 1 :]
            if not number:
                break
            idx = number.index(max(number))
        else:
            idx = number.index(max(number[:idx]))

    return value


# stack을 활용한 풀이
def solution(number, k):

    if not number:
        return 0

    stack = []

    for i in number:

        if not stack:
            stack.append(i)
            continue

        while stack:
            if stack[-1] < i and k > 0:
                stack.pop()
                k -= 1
                continue
            else:
                break

        stack.append(i)

    if k:
        stack = stack[:-k]

    return "".join(stack)

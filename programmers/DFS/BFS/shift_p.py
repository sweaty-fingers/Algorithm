from collections import deque


def split_u_v(p):

    if not p:
        return ""

    u = []
    stack = []
    v = deque(p)
    stack.append(v.popleft())
    u.append(stack[-1])
    shift = 0

    while stack and v:
        nxt = v.popleft()

        if stack[-1] != nxt:
            stack.pop()
            shift += 1
        elif stack[-1] == nxt:
            stack.append(nxt)
        u.append(nxt)

    # print("".join(u))

    u = "".join(u)
    v = "".join(v)

    if u[0] == "(":
        return u + split_u_v(v)
    else:
        return "(" + split_u_v(v) + ")" + reverse_p(u[1:-1])


def reverse_p(p):
    ans = ""
    for i in p:
        if i == "(":
            ans += ")"
        if i == ")":
            ans += "("
    return ans


def solution(p):
    return split_u_v(p)

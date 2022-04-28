# https://programmers.co.kr/learn/courses/30/lessons/60058
# 프로그래머스 괄호 변환
def reverse_p(p):
    result = ""

    for s in p:
        if s == "(":
            result += ")"
        else:
            result += "("

    return result


def solution(p):

    if not p:
        return p

    count = 0
    result = ""

    for i, s in enumerate(p):
        if s == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            u, v = p[: i + 1], p[i + 1 :]

            if u[0] == "(":
                result += u + solution(v)
            else:
                temp = "("
                temp += solution(v)
                temp += ")"
                temp += reverse_p(u[1:-1])
                result += temp

            break

    return result

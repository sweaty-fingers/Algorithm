def solution(n, lost, reserve):
    answer = 0

    if not lost or n ==0:
        return n

    lost.sort()
    reserve.sort()

    got_uniform = set()
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            got_uniform.add(i)

    for i in lost:
        if i in got_uniform:
            continue

        if i - 1 in reserve:
            reserve.remove(i - 1)
            got_uniform.add(i - 1)
            continue
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            got_uniform.add(i + 1)
            continue

    return n - (len(lost) - len(got_uniform))

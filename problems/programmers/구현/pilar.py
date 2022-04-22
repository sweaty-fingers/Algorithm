# 프로그래머스 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061


def test_building(x, y, a, results):
    is_ok = False
    if a == 0:
        if y == 0 or [x, y - 1, 0] in results or [x - 1, y, 1] in results or [x, y, 1] in results:
            is_ok = True
    if a == 1:
        if [x - 1, y, 1] in results and [x + 1, y, 1] in results:
            is_ok = True
        if [x, y - 1, 0] in results or [x + 1, y - 1, 0] in results:
            is_ok = True

    return is_ok


def solution(n, build_frame):

    results = []

    for x, y, a, b in build_frame:
        test_build = []

        if b:
            if [x, y, a] in results:
                continue
            test_build.append([x, y, a])
        else:
            if not [x, y, a] in results:
                continue

            results.remove([x, y, a])
            if a == 0:
                test_build.append([x, y + 1, 1])
                test_build.append([x - 1, y + 1, 1])
                test_build.append([x, y + 1, 0])
            elif a == 1:
                test_build.append([x - 1, y, 1])
                test_build.append([x + 1, y, 1])
                test_build.append([x, y, 0])
                test_build.append([x + 1, y, 0])

        for t_build in test_build:
            if b:
                is_ok = test_building(*t_build, results)
                if is_ok == True:
                    results.append(t_build)

            else:
                if not t_build in results:
                    continue
                results.remove(t_build)
                is_ok = test_building(*t_build, results)
                results.append(t_build)

                if not is_ok:
                    results.append([x, y, a])
                    break

    results.sort()

    return results

# https://www.acmicpc.net/problem/18428
# 감시 피하기

import logging
from collections import deque
from copy import deepcopy

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.WARNING)

RESULT = False
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_input():
    global T_POS

    N = int(input())
    graph = [list(map(str, input().split(" "))) for _ in range(N)]

    T_POS = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "T":
                T_POS.append((i, j))

    return graph


def bfs(graph):
    global RESULT

    is_escape = True
    q = deque([])

    for y, x in T_POS:
        for m in range(len(move)):
            q.append((y, x, m))

            while q:
                y_cur, x_cur, m = q.popleft()

                dy, dx = move[m]
                y_tmp, x_tmp = y_cur + dy, x_cur + dx

                if not ((0 <= y_tmp < len(graph)) and (0 <= x_tmp < len(graph[0]))):
                    continue

                if graph[y_tmp][x_tmp] == "O" or graph[y_tmp][x_tmp] == "T":
                    continue

                q.append((y_tmp, x_tmp, m))

                if graph[y_tmp][x_tmp] == "S":
                    is_escape = False

    if is_escape:
        root_logger.info(f"escape: {is_escape}")
        for g in graph:
            root_logger.info(g)
        root_logger.info("-" * 20)
        RESULT = True


def check(graph, count=0):

    if count == 3:
        bfs(deepcopy(graph))

    else:
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == "X":
                    graph[i][j] = "O"
                    count += 1
                    check(graph, count)
                    graph[i][j] = "X"
                    count -= 1


def main():
    graph = get_input()
    count = 0

    check(graph, count)

    if RESULT:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

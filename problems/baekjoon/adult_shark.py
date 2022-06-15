move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
move_str = ["up", "down", "left", " right"]

import logging
from collections import deque

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.INFO)

K = 0
shark_moves = []
shark_direct = []
result = 0


def get_input():
    global K
    global shark_moves
    global shark_direct

    n, m, K = map(int, input().split(" "))

    graph = [[] for _ in range(n)]
    shark_dict = {i + 1: deque([]) for i in range(m)}
    for i in range(n):
        row = list(map(int, input().split(" ")))
        for j, r in enumerate(row):
            graph[i].append(r)
            if r != 0:
                shark_dict[r].append((i, j))

    shark_direct = [0] + list(map(int, input().split(" ")))

    shark_moves = {i: [] for i in range(1, m + 1)}

    for i in range(1, m + 1):
        shark_moves[i] = [tuple(map(int, input().split(" "))) for _ in range(4)]

    return graph, shark_dict


def remove_idx(shark, graph):
    global K

    if len(shark) >= K + 1:
        ry, rx = shark.popleft()
        if (ry, rx) not in shark:
            graph[ry][rx] = 0


def move_shark(graph, shark_dict):
    global shark_moves
    global shark_direct
    global K
    global result

    n = len(graph)
    m = len(shark_dict)
    n_shark = 0
    for i in range(1, m + 1):
        if not shark_dict[i]:
            continue

        n_shark += 1
        y, x = shark_dict[i][-1]
        direct = shark_direct[i]

        for di in shark_moves[i][direct]:
            y_tmp, x_tmp = y + move[di - 1][0], x + move[di - 1][1]

            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue

            if graph[y_tmp][x_tmp] == 0:
                shark_direct[i] = di
                shark_dict[i].append((y_tmp, x_tmp))
                remove_idx(shark_dict[i], graph)
                break

        for di in shark_moves[i][direct]:
            y_tmp, x_tmp = y + move[di - 1][0], x + move[di - 1][1]

            if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                continue

            if graph[y_tmp][x_tmp] == i:
                shark_direct[i] = di
                shark_dict[i].append((y_tmp, x_tmp))
                remove_idx(shark_dict[i], graph)
                break

    if n_shark == 1:
        return result

    other_sharks = []
    for i in range(1, len(shark_dict) + 1):
        y, x = shark_dict[i][-1]
        if (y, x) in other_sharks:
            shark_dict[i] = []
        else:
            other_sharks.append((y, x))

    result += 1

    move_shark(graph, shark_dict)


def main():
    graph, shark_dict = get_input()

    root_logger.info("")
    root_logger.info("graph")
    for g in graph:
        root_logger.info(g)

    root_logger.info(shark_dict)
    
    print(move_shark(graph, shark_dict))


if __name__ == "__main__":
    main()

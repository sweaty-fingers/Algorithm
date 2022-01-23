# from collections import deque
# import itertools

# move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # D 면 +1, L이면 -1

# def get_input():

#     N = int(input("N : "))
#     K = int(input("K : "))
#     loc_apples = []

#     for _ in range(K):
#         loc_apple = list(map(int, input("loc_appple : ").split(" ")))
#         loc_apples.append(tuple(loc_apple))

#     L = int(input("L :"))

#     directions = deque()
#     for _ in range(L):
#         time, direction = input("Direction : ").split(" ")
#         time = int(time)
#         directions.append((time, direction))

#     return N, loc_apples, directions


# if __name__ == "__main__":

#     N, loc_apples, directions = get_input() # 맵의 크기, 사과 위치, 방향전환

#     snake = deque([(1, 1)]) # 뱀이 차지하는 좌표
#     time = 0
#     idx_direct = 0
#     while True:
#         time += 1

#         dy, dx = move[idx_direct]
#         y, x = snake[-1]
#         head_y, head_x = y + dy, x + dx

#         print(f"snake : {snake!r}")
#         print(f"y, x : {head_y!r}, {head_x!r}")
#         if not (head_x <= N and head_y <= N and head_x >= 1 and head_y >= 1) or (head_y, head_x) in list(itertools.islice(snake, len(snake)-1)):
#             break

#         if (head_y, head_x) in loc_apples:
#             snake.append((head_y, head_x))
#             loc_apples.remove((head_y, head_x))
#         else:
#             snake.append((head_y, head_x))
#             snake.popleft()


#         if directions and time == directions[0][0]:
#             t, dir = directions.popleft()

#             print(f"time: {time!r}, move_dir: {dir!r}")

#             if dir == "L":
#                 idx_direct = (idx_direct - 1) % 4

#             else:
#                 idx_direct = (idx_direct + 1) % 4

#     print(time)

from collections import deque
import itertools

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # D 면 +1, L이면 -1


def get_input():

    N = int(input())
    K = int(input())
    loc_apples = []

    for _ in range(K):
        loc_apple = list(map(int, input().split(" ")))
        loc_apples.append(tuple(loc_apple))

    L = int(input())

    directions = deque()
    for _ in range(L):
        time, direction = input().split(" ")
        time = int(time)
        directions.append((time, direction))

    return N, loc_apples, directions


if __name__ == "__main__":

    N, loc_apples, directions = get_input()  # 맵의 크기, 사과 위치, 방향전환

    snake = deque([(1, 1)])  # 뱀이 차지하는 좌표
    time = 0
    idx_direct = 0
    while True:
        time += 1

        dy, dx = move[idx_direct]
        y, x = snake[-1]
        head_y, head_x = y + dy, x + dx

        if not (head_x <= N and head_y <= N and head_x >= 1 and head_y >= 1) or (
            head_y,
            head_x,
        ) in list(itertools.islice(snake, len(snake) - 1)):
            break

        if (head_y, head_x) in loc_apples:
            snake.append((head_y, head_x))
            loc_apples.remove((head_y, head_x))
        else:
            snake.append((head_y, head_x))
            snake.popleft()

        if directions and time == directions[0][0]:
            t, dir = directions.popleft()

            if dir == "L":
                idx_direct = (idx_direct - 1) % 4

            else:
                idx_direct = (idx_direct + 1) % 4

    print(time)

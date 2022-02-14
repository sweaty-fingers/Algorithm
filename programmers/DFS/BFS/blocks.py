from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def move_parallel(board, cur):

    next_ = []
    (y_p, x_p), (y_r, x_r) = cur

    # 평행 이동
    for dy, dx in move:
        y_p_temp, x_p_temp, y_r_temp, x_r_temp = y_p + dy, x_p + dx, y_r + dy, x_r + dx

        if is_out_of_bound(board, y_p_temp, x_p_temp, y_r_temp, x_r_temp):
            continue

        if is_wall(board, y_p_temp, x_p_temp, y_r_temp, x_r_temp):
            continue

        next_.append({(y_p_temp, x_p_temp), (y_r_temp, x_r_temp)})

    return next_


def rotate(board, cur):
    next_ = []
    (y_p, x_p), (y_r, x_r) = cur

    if y_p == y_r:

        if not is_out_of_bound(board, y_p + 1, x_p, y_r, x_r) and not is_wall(
            board, y_p + 1, x_p, y_r + 1, x_r
        ):
            next_.append({(y_p, x_p), (y_p + 1, x_p)})
            next_.append({(y_r + 1, x_r), (y_r, x_r)})

        if not is_out_of_bound(board, y_p - 1, x_p, y_r, x_r) and not is_wall(
            board, y_p - 1, x_p, y_r - 1, x_r
        ):
            next_.append({(y_p, x_p), (y_p - 1, x_p)})
            next_.append({(y_r - 1, x_r), (y_r, x_r)})

    if x_p == x_r:

        if not is_out_of_bound(board, y_p, x_p + 1, y_r, x_r) and not is_wall(
            board, y_p, x_p + 1, y_r, x_r + 1
        ):
            next_.append({(y_p, x_p), (y_p, x_p + 1)})
            next_.append({(y_r, x_r + 1), (y_r, x_r)})

        if not is_out_of_bound(board, y_p, x_p - 1, y_r, x_r) and not is_wall(
            board, y_p, x_p - 1, y_r, x_r - 1
        ):
            next_.append({(y_p, x_p), (y_p, x_p - 1)})
            next_.append({(y_r, x_r - 1), (y_r, x_r)})

    return next_


def is_out_of_bound(board, y1, x1, y2, x2):
    if not (
        0 <= y1 < len(board)
        and 0 <= x1 < len(board)
        and 0 <= y2 < len(board)
        and 0 <= x2 < len(board)
    ):
        return True

    return False


def is_wall(board, y1, x1, y2, x2):
    if board[y1][x1] == 1 or board[y2][x2] == 1:
        return True

    return False


def is_end(board, cur):
    for y, x in cur:
        if y == len(board) - 1 and x == len(board) - 1:
            return True

    return False


def bfs(board):
    queue = deque([])
    queue.append([{(0, 0), (0, 1)}, 0])  # [y1, x1, y2, x2, t]
    visited = [{(0, 0), (0, 1)}]

    while queue:
        cur, t = queue.popleft()
        next_ = []

        if is_end(board, cur):
            return t

        next_.extend(move_parallel(board, cur))
        next_.extend(rotate(board, cur))

        for cur in next_:
            if cur not in visited:
                queue.append([cur, t + 1])
                visited.append(cur)


def solution(board):
    return bfs(board)

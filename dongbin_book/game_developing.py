# 이것이 코딩테스트다 구현 실전문제 3 개임개발.

if __name__ == "__main__":
    max_row, max_col = map(int, input().split())
    visited = [[0] * max_col for _ in range(max_row)]

    y, x, direction = map(int, input().split())
    visited[y][x] = 1

    map_ = []
    for i in range(max_row):
        map_.append(list(map(int, input().split())))

    # 이동가능 방향

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    count = 1

    max_turn = 4
    num_turn = 0

    while True:

        direction -= 1
        if direction == -1:
            direction = 3

        x_temp = x + dx[direction]
        y_temp = y + dy[direction]

        if visited[y_temp][x_temp] == 0 and map_[y_temp][x_temp] == 0:  # 방문 안함 & 육지
            visited[y_temp][x_temp] = 1
            y = y_temp
            x = x_temp
            count += 1
            num_turn = 0
            continue
        else:
            num_turn += 1

        if num_turn == 4:
            x_temp = x - dx[direction]
            y_temp = y - dy[direction]
            
            if map_[x_temp][y_temp] == 1:
                break
            
            x = x_temp
            y = y_temp

            num_turn = 0


    print(count)

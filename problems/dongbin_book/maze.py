# 이것이 코딩테스트다 DFS/BFS 실전 문제 미로찾기

from collections import deque

def bfs(start):
    global map_

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    queue = deque([start])

    while queue:
        position = queue.popleft()
        x, y = position

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >=n or map_[ny][nx] != 1:
                continue
            
            queue.append((nx, ny))
            map_[ny][nx] = map_[y][x] + 1

    return map_[n-1][m-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    map_ = []
    for i in range(n):
        map_.append(list(map(int,input())))

    start = (0, 0)
    result = bfs(start)

    print(result)
# 이것이 코딩테스트다 DFS/BFS 실전문제 1 음료수 얼려 먹기

def dfs(x, y):
    global filled
    global n, m

    filled[y][x] = 1

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n and filled[ny][nx] == 0:
            print("done")
            dfs(nx, ny)


if __name__ == "__main__":

    n, m = map(int, input().split())

    filled = []
    for i in range(n):
        filled.append(list(map(int, input().split())))

    count = 0

    for i in range(n):
        for j in range(m):
            if filled[i][j] == 0:
                count += 1
                dfs(j, i)
                for row in filled:
                    print(row)
                print()

    print(count)

    

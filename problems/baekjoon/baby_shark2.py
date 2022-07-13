from collections import deque

MOVE = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def get_input():
    n, m = map(int, input().split(" "))
    
    graph = [list(map(int, input().split(" "))) for _ in range(n)]
    
    return graph


def bfs(graph):
    
    n = len(graph)
    m = len(graph[0])

    max_d = 0
    
    for i in range(n):
        for j in range(m):
            
            if graph[i][j] != 0:
                continue
            q = deque([(i, j, 0)]) # y, x, distance
            seen = {(i, j)}
            
            while q:
                
                y, x, d = q.popleft()
                # print(y, x, d)
                
                if graph[y][x] == 1:
                    max_d = max(max_d, d)
                    break        

                for dy, dx in MOVE:
                    y_tmp, x_tmp = y + dy, x + dx
                    
                    if not ((0 <= y_tmp < n) and (0 <= x_tmp < m)):
                        continue
                    
                    if (y_tmp, x_tmp) in seen:
                        continue
                    
                    # print(y_tmp, x_tmp, d)
                    # input()
                    q.append((y_tmp, x_tmp, d + 1))
                    seen.add((y_tmp, x_tmp))

    return max_d
    

def main():
    graph = get_input()
    d = bfs(graph)
    print(d)
    

if __name__ == "__main__":
    main()
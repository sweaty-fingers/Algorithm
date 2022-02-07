from collections import deque

move = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def get_input():
    N, K = map(int, input().split(" "))
    
    mapped = [list(map(int, input().split(" "))) for _ in range(N)]
    map_with_time = []
    for row in mapped:
        row_temp = []
        for c in row:
            row_temp.append([c, 0])
        map_with_time.append(row_temp)
            
    S, Y, X = map(int, input().split(" "))
    
    # for row in map_with_time:
    #     print(f"{row!r}")
    
    #print(f"virus at 0, 0 : {map_with_time[0][0][0]}, time: {map_with_time[0][0][1]}")
    
    return map_with_time, N, K, S, Y, X

def fill_virus(mapped, k, y, x, S):
    N = len(mapped)
    queue = deque([(y, x)])
    
    while queue:
        y, x = queue.popleft()
        
        if mapped[y][x][1] >= S:
            return
            
        for dx, dy in move:
            x_temp, y_temp = x + dx, y + dy
            
            if x_temp < 0 or x_temp >= N or y_temp < 0 or y_temp >= N:
                continue
            
            if mapped[y_temp][x_temp][0] == 0:
                mapped[y_temp][x_temp][0] = k
                mapped[y_temp][x_temp][1] = mapped[y][x][1] + 1
                queue.append((y_temp, x_temp))
                
            elif mapped[y_temp][x_temp][0] < k and mapped[y_temp][x_temp][1] > mapped[y][x][1] + 1:
                mapped[y_temp][x_temp][0] = k
                mapped[y_temp][x_temp][1] = mapped[y][x][1] + 1
                queue.append((y_temp, x_temp))

def main():
    mapped, N, K, S, Y, X = get_input()
    
 
    for k in range(1, K + 1):
        for y in range(N):
            for x in range(N):
                if mapped[y][x][0] == k:
                    fill_virus(mapped, k, y, x, S)
    
    # r = ""
    # for y in range(N):
    #     for x in range(N):
    #         r += str(mapped[y][x][0]) + " "
    #     print(r)
    #     r=""
    print(mapped[Y-1][X-1][0])
        

if __name__ == "__main__":
    main()

    
    
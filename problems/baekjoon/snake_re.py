from collections import deque

move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right: +1, left: -1

def get_input():
    N = int(input())
    map_array = [[0] * (N + 1) for _ in range(N + 1)]
    k = int(input())
    
    map_array[1][1] = 1
    for _ in range(k):
        r, c = map(int, input().split(" "))
        map_array[r][c] = 2
    
    m = int(input())
    move_list = []
    for _ in range(m):
        t, d = input().split(" ")
        t = int(t)
        move_list.append((t, d))
    
    move_list = deque(move_list)
    
    return map_array, move_list


def main():
    map_array, move_list = get_input()
    n = len(map_array)
    t_cur = 0
    t_to_change, direction = move_list.popleft()
    d_index = 0

    y_head, x_head = 1, 1
    dy_head, dx_head = move[d_index]
    snake = deque([(y_head, x_head)])
    
    while 1:
        
        
        y_temp, x_temp = y_head + dy_head, x_head + dx_head
        if not ((1 <= y_temp < n) and (1 <= x_temp < n)):
            return t_cur + 1
        
        if map_array[y_temp][x_temp] == 1:
            return t_cur + 1
        
        if map_array[y_temp][x_temp] == 0:
            y_tail, x_tail = snake.popleft()
            map_array[y_tail][x_tail] = 0
            
        map_array[y_temp][x_temp] = 1
        y_head, x_head = y_temp, x_temp
        snake.append((y_head, x_head))
        # print(f"snake: {snake}")
        
        t_cur += 1
        if t_cur == t_to_change:
            
            if direction == "L":
                d_index = (d_index - 1) % 4
            elif direction == "D":
                d_index = (d_index + 1) % 4
            else:
                raise "need to input exact directions ('L' or 'D')"
                
            dy_head, dx_head = move[d_index]
            if move_list:
                t_to_change, direction = move_list.popleft()

        # print(t_cur)
        # for m in map_array:
        #     print(m)
        # print("-" * 30)
    
        
if __name__ == "__main__":
    print(main())
    
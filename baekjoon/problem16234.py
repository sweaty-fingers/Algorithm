from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_input():
    N, L, R = map(int, input().split(" "))
    
    mapped = [list(map(int, input().split(" "))) for _ in range(N)]
    
    return mapped, L, R

def bfs(mapped, y, x, L, R, link):
    queue = deque([(y, x)])    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in move:
            y_temp, x_temp = y + dy, x + dx
            
            if y_temp < 0 or y_temp >= len(mapped) or x_temp < 0 or x_temp >= len(mapped):
                continue
            
            if abs(mapped[y_temp][x_temp] - mapped[y][x]) <= R and abs(mapped[y_temp][x_temp] - mapped[y][x]) >= L and (y_temp, x_temp) not in link:
                link.append((y_temp, x_temp))
                queue.append((y_temp, x_temp))
    
    return link
        
def check_and_move(mapped, t, l, r):
    while True:
        links = []
        link = []
        for y in range(len(mapped)):
            for x in range(len(mapped)):
                if (y, x) in link:
                    continue
                link = []
                link = bfs(mapped, y, x, l, r, link)
                if link and link not in links:
                    links.append(link)
                        
        if links:
            for link in links:
                sum_ = 0
                for y, x in link:
                    sum_ += mapped[y][x]
                # print(f"sum : {sum_}")
                # print(f"len : {len(link)}")
                mean = sum_ // len(link)
            
                for y, x in link:
                    mapped[y][x] = mean
            
            t += 1
            
            # for row in mapped:
            #     print(f"{row!r}")
            # print("-" * 60)
            
        else:
            return t
        
def main():
    mapped, L, R = get_input()
    t = 0
    t = check_and_move(mapped, t, L, R)
    print(t)
    

if __name__ == "__main__":
    main()
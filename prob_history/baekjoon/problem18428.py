move = [(1, 0), (0, 1), (-1, 0), (0, -1)] # (dy, dx) URDL

def get_input():
    N = int(input())
    mapped = [input().split(" ") for _ in range(N)]
    
    return mapped

def find_students(mapped, y, x, to=None):
    stack = [(y, x)]
    
    while stack:
        cur = stack.pop()
        
        y_temp, x_temp = cur[0] + move[to][0], cur[1] + move[to][1]
        
        if y_temp < 0 or y_temp >= len(mapped) or x_temp < 0 or x_temp >= len(mapped[0]):
            continue
        
        if mapped[y_temp][x_temp] == "S":
            return True
        
        if mapped[y_temp][x_temp] == "O":
            return False
        stack.append((y_temp, x_temp))
                
    return False
    
def set_obs_and_check(mapped, num_obs=0, answer=None):
    if not answer.is_find:
        return
    
    if num_obs == 3:
        for y in range(len(mapped)):
            for x in range(len(mapped[0])):
                if mapped[y][x] == 'T':
                    for to in range(len(move)):
                        is_find = find_students(mapped, y, x, to)
                        if is_find:
                            return
                                                
        # for row in mapped:
        #     print(f"{row!r}")
        # print("-" * 60)
        answer.is_find = False
            
    for y in range(len(mapped)):
        for x in range(len(mapped[0])):
            if mapped[y][x] == "X":
                mapped[y][x] = 'O'
                num_obs += 1
                set_obs_and_check(mapped, num_obs, answer)
                mapped[y][x] = 'X'
                num_obs -= 1
    
        
class Result:
    def __init__(self):
        self.is_find = True

def main():
    mapped = get_input()
    answer = Result()
    
    set_obs_and_check(mapped, num_obs=0, answer=answer)

    if not answer.is_find:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
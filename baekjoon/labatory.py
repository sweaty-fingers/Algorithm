move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_map():
    N, M = map(int, input().split(" "))

    map_list = []
    for _ in range(N):
        map_list.append(list(map(int, input().split(" "))))

    return map_list


def fill_virus(map_list, x, y):
    """
    dfs 탐색 실행
    parameters
    ----------
    target : 채울 요소
        1 : wall, 2 : virus
    """

    y_limit = len(map_list)
    x_limit = len(map_list[0])

    stack = []
    stack.append((x, y))

    while stack:
        x, y = stack.pop()

        for dx, dy in move:
            x_temp, y_temp = x + dx, y + dy

            if x_temp < 0 or x_temp >= x_limit or y_temp < 0 or y_temp >= y_limit:
                continue
    
            if map_list[y_temp][x_temp] == 0:
                map_list[y_temp][x_temp] = 2
                stack.append((x_temp, y_temp))
            
    return map_list


def get_count(map_list):
    count = 0
    for y in range(len(map_list)):
        for x in range(len(map_list[0])):
            if map_list[y][x] == 0:
                count += 1
                
    # print("Fill virus")
    # for row in map_list:
    #     print(row)
    # print(f"count : {count}")
    # print("-" * 40)

    return count

def set_wall_and_check(map_list, wall_count=0, result=None):
    
    if wall_count == 3:
        map_virus = [[0] * len(map_list[0]) for _ in range(len(map_list))]
        
        for i in range(len(map_list)):
            map_virus[i] = map_list[i][:]
        
        for y in range(len(map_virus)):
            for x in range(len(map_virus[0])):
                if map_virus[y][x] == 2:
                    fill_virus(map_virus, x, y)
        
        result.answer = max(get_count(map_virus), result.answer)
        #print(result.answer)
        return
    
    for y in range(len(map_list)):
        for x in range(len(map_list[0])):
            if map_list[y][x] == 0:
                map_list[y][x] = 1
                wall_count += 1
                # print("add_wall")
                # for row in map_list:
                #     print(row)
                set_wall_and_check(map_list, wall_count=wall_count, result=result)
                map_list[y][x] = 0
                wall_count -= 1
                # print("remove_wall")
                # for row in map_list:
                #     print(row)
                
class Result:
    def __init__(self, answer=0):
        self.answer = answer

def main():
    
    map_list = get_map()
    result = Result(0)
    wall_count = 0
    set_wall_and_check(map_list, wall_count=wall_count, result=result)

    print(result.answer)


if __name__ == "__main__":
    main()

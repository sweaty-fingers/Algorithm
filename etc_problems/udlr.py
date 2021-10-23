# 이것이 코딩테스트다 구현 예제 1

if __name__ == "__main__":
    N = input()
    move_list = list(map(str, input().split()))

    position = [1, 1]

    for move in move_list:
        
        if move == 'R' and position[1] < 5:
            print(f"position {position} to")
            position[1] += 1
            print(f"{position}")
        elif move == "L" and position[1] > 1:
            print(f"position {position} to")
            position[1] -= 1
            print(f"{position}")
        elif move == "D" and position[0] < 5:
            print(f"position {position} to")
            position[0] += 1 
            print(f"{position}")
        elif move == "U" and position[0] > 1:
            print(f"position {position} to")
            position[0] -= 1
            print(f"{position}")

    print(position)



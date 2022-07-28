def get_input():
    n = int(input())
    sharks = [tuple(map(int, input().split(" "))) for _ in range(n)]
    
    return sharks


def dinner(sharks):
    shark_map = [1] * len(sharks)
    shark_eat = [0] * len(sharks)
    
    for i in range(1, len(sharks)):
        for j in range(i):
            if shark_map[j] == 0 or shark_map[i] == 0 or shark_eat[i] >= 2:
                continue
            
            if (sharks[j][0] <= sharks[i][0] and sharks[j][1] <= sharks[i][1] and sharks[j][2] <= sharks[i][2]):
                shark_map[j] = 0
                shark_eat[i] += 1
    
    return sum(shark_map)

def main():
    
    sharks = get_input()
    # print("shark")
    # print(f"{sharks}")
    
    sharks = sorted(sharks, key=lambda x: (x[0], x[1], x[2]))
    
    # print(sharks)
    
    print(dinner(sharks))

if __name__ == "__main__":
    main()
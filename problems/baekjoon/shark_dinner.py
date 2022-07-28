def get_input():
    n = int(input())
    sharks = [tuple(map(int, input().split(" "))) for _ in range(n)]
    graph = [[] for _ in range(n)]
        
    return sharks, graph


def make_graph(sharks, graph):
    shark_map = [1] * len(sharks)
    shark_eat = [0] * len(sharks)
    
    for i in range(1, len(sharks)):
        for j in range(i):
            
            if (sharks[j][0] <= sharks[i][0] and sharks[j][1] <= sharks[i][1] and sharks[j][2] <= sharks[i][2]):
                shark_map[j] = 0
                shark_eat[i] += 1
    
    return sum(shark_map)

def main():
    
    sharks, graph = get_input()
    # print("shark")
    # print(f"{sharks}")
    
    # print(sharks)
    print(dinner(sharks))
    print(graph)
    
if __name__ == "__main__":
    main()
# https://www.acmicpc.net/problem/11404
# 백준 플로이드

INF = 1e9

def get_input():
    n = int(input())
    m = int(input())
    
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):    
        graph[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split(" "))
        
        graph[a][b] = min(c, graph[a][b])
        
    return graph


def floyd(graph):
    n = len(graph)
    
    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


def main():
    graph = get_input()
    graph = floyd(graph)
    n = len(graph)
    
    for i in range(1, n):
        for j in range(1, n):
            print(graph[i][j], end=" ")
        
        print("")
        

if __name__ == "__main__":
    main()
        
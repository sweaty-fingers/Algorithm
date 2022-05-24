# 동빈나 이코테 정확한 순위
INF = 1e9

def get_input():
    n, m = map(int, input().split(" ")) 
    graph = [[1] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 0
        

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
    
    members = [0] * n
    for i in range(1, n):
        for j in range(1, n):
            members[i] += graph[i][j]
            members[j] += graph[i][j]
        
    possible_members = [i for i in range(n) if members[i] == (n - 2)]

    print(len(possible_members))

if __name__ == "__main__":
    main()
    
INF = 1e9
def get_input():
    n, m = map(int, input().split(" "))

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(1, n + 1):
        graph[_][_] = 0

    for _ in range(m):
        a, b = map(int, input().split(" "))
        graph[a][b] = 1

    return n, graph

def floyd(n, graph):

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

def get_num(n, graph):

    sum_ = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                graph[i][j] = 0
            else:
                graph[i][j] = 1

            sum_[i] += graph[i][j]
            sum_[j] += graph[i][j]
    
    results = [i for i in range(1, n + 1) if sum_[i] == n - 1]

    return len(results)

def main():
    n, graph = get_input()
    graph = floyd(n, graph)
    print(get_num(n, graph))
    
if __name__ == "__main__":
    main()
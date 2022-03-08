INF = 1e9
def get_input():
    n = int(input())
    m = int(input())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split(" "))
        graph[a][b] = min(graph[a][b], c)

    
    return n, graph


def floyd(n, graph):

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


def main():
    n, graph = get_input()

    graph = floyd(n, graph)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                print(0, end=" ")
            else:
                print(graph[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
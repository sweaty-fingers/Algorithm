from collections import deque


def get_input():

    n = int(input())
    prev_score = list(map(int, input().split(" ")))

    graph = [[] for _ in range(n + 1)]
    n_degree = [0] * (n + 1)

    for i in range(len(prev_score)):
        for j in range(i + 1, len(prev_score)):
            graph[prev_score[i]].append(prev_score[j])
            n_degree[prev_score[j]] += 1

    m = int(input())

    for i in range(m):
        a, b = map(int, input().split(" "))

        if prev_score.index(a) < prev_score.index(b):
            graph[a].remove(b)
            n_degree[b] -= 1
            graph[b].append(a)
            n_degree[a] += 1
        else:
            graph[b].remove(a)
            n_degree[a] -= 1
            graph[a].append(b)
            n_degree[b] += 1

    return graph, n_degree


def topology(graph, n_degree):
    result = []
    q = deque([])
    n = len(n_degree) - 1

    for i in range(1, n + 1):
        if n_degree[i] == 0:
            q.append(i)

    for _ in range(n):

        if len(q) > 1:
            return "?"

        if len(q) == 0:
            return "IMPOSSIBLE"

        node = q.popleft()

        result.append(str(node))

        for to in graph[node]:
            n_degree[to] -= 1
            if n_degree[to] == 0:
                q.append(to)

    return " ".join(result) if result else "IMPOSSIBLE"


def main():
    n = int(input())

    results = []
    for _ in range(n):
        graph, n_degree = get_input()
        results.append(topology(graph, n_degree))

    for r in results:
        print(r)


if __name__ == "__main__":
    main()

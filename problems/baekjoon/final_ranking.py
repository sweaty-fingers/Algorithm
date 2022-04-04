from collections import deque


def get_input():
    n_team = int(input())
    last_ranking = list(map(int, input().split(" ")))

    graph = [[] for _ in range(n_team + 1)]
    indegree = [0] * (n_team + 1)

    for i in range(len(last_ranking)):
        for j in range(i + 1, len(last_ranking)):
            graph[last_ranking[i]].append(last_ranking[j])
            indegree[last_ranking[j]] += 1

    # print(f"graph: {graph}")
    # print(f"indegree: {indegree}")
    n_change = int(input())

    for _ in range(n_change):
        a, b = map(int, input().split(" "))

        if last_ranking.index(a) < last_ranking.index(b):
            graph[b].append(a)
            indegree[a] += 1
            graph[a].remove(b)
            indegree[b] -= 1
        else:
            graph[a].append(b)
            indegree[b] += 1
            graph[b].remove(a)
            indegree[a] -= 1

    return n_team, graph, indegree


def topology_sort(n_team, graph, indegree):
    final_ranking = []
    q = deque([])

    for i in range(1, n_team + 1):
        if indegree[i] == 0:
            q.append(i)

    for _ in range(n_team):
        if len(q) > 1:
            # print("?")
            return "?"

        if len(q) == 0:
            return "IMPOSSIBLE"

        now = q.popleft()

        final_ranking.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return final_ranking if final_ranking else "IMPOSSIBLE"


def main():
    n_test = int(input())

    results = []
    for _ in range(n_test):
        n_team, graph, indegree = get_input()
        # print(f"n_team: {n_team}")
        # print(f"graph: {graph}")
        # print(f"indegree: {indegree}")
        results.append(topology_sort(n_team, graph, indegree))
        # print(results[-1])

    # print(" ")
    # print(f"{results}")
    for result in results:
        if isinstance(result, list):
            print(" ".join(list(map(str, result))))
        else:
            print(f"{result}")


if __name__ == "__main__":
    main()

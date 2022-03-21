import heapq

INF = 1e9

def get_input():
    n, m = map(int, input().split(" "))

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split(" "))
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    return n, graph

def get_answer(n, graph):
    distance = [INF] * (n + 1)
    heap = []

    heapq.heappush(heap, (0, 1))
    distance[1] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for g in graph[now]:
            dist_tmp = dist + g[1]

            if dist_tmp < distance[g[0]]:
                distance[g[0]] = dist_tmp
                heapq.heappush(heap, (dist_tmp, g[0]))

    
    node_distance = []
    for i in range(1, n + 1):
        node_distance.append((distance[i], i))
    
    print(node_distance)
    node_distance = sorted(node_distance, key=lambda x: x[1], reverse=True)
    node_distance = sorted(node_distance, key=lambda x: x[0])
    print(node_distance)
    dist, node  = node_distance[-1][0], node_distance[-1][1]

    num_results = 0
    for i in reversed(range(len(node_distance))):
        if node_distance[i][0] == dist:
            num_results += 1
        else:
            break

    print(node, dist, num_results)

def main():
    n, graph = get_input()
    get_answer(n, graph)


if __name__ == "__main__":
    main()
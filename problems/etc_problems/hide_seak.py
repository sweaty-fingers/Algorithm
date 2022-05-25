import heapq
INF = 1e9

def get_input():
    n, m = map(int, input().split(" "))
    
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split(" "))
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        
        
    return graph, distance
    
    
def dijstra(graph, distance, start=1):
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, cur = heapq.heappop(q)
        
        if dist > distance[cur]:
            continue
        
        for g in graph[cur]:
            to, cost = g
            cost = cost + dist
            
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(q, (cost, to))
    
    return distance
        


def main():
    graph, distance = get_input()
    distance = dijstra(graph, distance)
    max_dist = 0
    prev_max = max_dist
    nodes = []
    for i, d in enumerate(distance):
        if d == INF:
            continue
        max_dist = max(max_dist, d)
        if max_dist > prev_max:
            nodes = [i]
            prev_max = max_dist
        elif max_dist == prev_max:
            nodes.append(i)

    
    nodes.sort()
    print(f"{nodes[0]} {max_dist} {len(nodes)}")
        


if __name__ == "__main__":
    main()
    

# input
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
# https://www.acmicpc.net/problem/18352

from collections import defaultdict, deque

def get_input():
    graph = defaultdict(list)
    N, M, K, X = map(int, input().split(" "))

    for _ in range(M):
        f, to = map(int, input().split(" "))
        graph[f].append(to)
    
    return N, K, X, graph

def get_cities(X, K, graph):
    q = deque([])
    seen = set()
    cities = set()
    q.append((X, 0))
    while q:
        city, dist = q.popleft()
        # print(f"city : {city!r}, dist : {dist!r}")
        if dist == K:
            return cities
            
        for c in graph[city]:
            if c not in seen:
                seen.add(c)
                q.append((c, dist + 1))

                if dist + 1 == K and c != X:
                    cities.add(c)

                    # print(f"cities : {cities!r}")

    return cities
            
def main():
    N, K, X, graph = get_input()
    cities = list(get_cities(X, K, graph))
    
    if not cities:
        print(-1)

    else:
        cities.sort()
        for c in cities:
            print(c)

if __name__ == "__main__":
    main()
     
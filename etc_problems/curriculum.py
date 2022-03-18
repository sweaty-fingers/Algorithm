from collections import deque

def get_input():
    n = int(input())

    subjects = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        subject = list(map(int, input().split(" ")))
        subjects[i] = [subject[0], subject[1:-1]] # cost, prerequir
    
    return n, subjects

def topology_sort(subjects, n):
    result = []
    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for b in range(1, n + 1):
        _, pre = subjects[b]
        for a in pre:
            graph[a].append(b)
            degree[b] += 1
    
    q = deque([])
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        cost, pre = subjects[now]

        if pre:
            cost_pre = max([subjects[c][0] for c in pre])
            cost += cost_pre
            subjects[now][0] = cost

        for i in graph[now]:
            degree[i] -= 1

            if degree[i] == 0:
                q.append(i)
    
    return subjects

def main():
    n, subjects = get_input()
    subjects = topology_sort(subjects, n)

    for i in range(1, n + 1):
        print(subjects[i][0])


if __name__ == "__main__":
    main()
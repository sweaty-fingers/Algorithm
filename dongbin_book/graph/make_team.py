def get_input():
    n, m = map(int, input().split(" "))

    opers = []
    for _ in range(m):
        opers.append(tuple(map(int, input().split(" "))))

    return n, opers


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def main():
    n, opers = get_input()
    parent = [0] * (n + 1)

    for i in range(n + 1):
        parent[i] = i

    for oper in opers:
        o, a, b = oper

        if o == 0:
            union_parent(parent, a, b)
        else:
            if find_parent(parent, a) == find_parent(parent, b):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()
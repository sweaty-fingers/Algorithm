# 이코테 책 그래프 문제: 탑승구

def get_inputs():
    g = int(input())
    p = int(input())
    dockings = []
    for _ in range(p):
        dockings.append(int(input()))

    return g, p, dockings

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def main():
    g, p, dockings = get_inputs()

    print(f"g: {g}")
    print(f"p: {p}")
    print(f"dockings: {dockings}")
    
    parent = [0] * (g + 1)
    num_parked = 0

    for i in range(1, g + 1):
        parent[i] = i

    for d in dockings:
        print(f"d: {d}")
        if find_parent(parent, d) == d:
            union_parent(parent, d, d - 1)
            num_parked += 1
            print(f"parent: {parent}")
            print(f"num_parked: {num_parked}")
            print()
            continue

        g_ = find_parent(parent, d) - 1
            
        if g_ < 0:
            return print(num_parked)
        else:
            union_parent(parent, d, g_)
            num_parked += 1        
            print(f"parent: {parent}")
            print(f"num_parked: {num_parked}")
        print()
    return print(num_parked)


if __name__ == "__main__":
    main()
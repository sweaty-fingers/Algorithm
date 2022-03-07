# https://www.acmicpc.net/problem/1932
move = [(1, 0), (1, 1)] # 왼쪽 아래 오른쪽 아래

def get_input():
    n = int(input())
    
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split(" "))))
    
    return n, li

def dy_program(li, n):

    results = []
    for i in range(n):
        results.append([0] * (i + 1))

    results[0][0] = li[0][0]

    for i in range(n - 1):
        for j in range(i + 1):
            #print("-" * 20)
            #print(f"i: {i}, j: {j}")
            for dy, dx in move:
                y_tmp, x_tmp = i + dy, j + dx
                #print(f"y_tmp: {y_tmp}, x_tmp: {x_tmp}")
                if not (0 <= y_tmp < n and 0 <= x_tmp < i + 2):
                    break
                #print("done")
                results[y_tmp][x_tmp] = max(results[y_tmp][x_tmp], li[y_tmp][x_tmp] + results[i][j])

    #for _ in range(n):
    #    print(f"{results[_]}")

    return max(results[n-1])

def main():
    n, li = get_input()
    print(dy_program(li, n))

if __name__ == "__main__":
    main()

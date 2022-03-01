move = [(-1, 1), (0, 1), (1, 1)] # 방향 설정, 오른쪽 위, 오른쪽, 오른쪽 아래

def get_inputs():
    n_test = int(input())
    
    li_total = []

    for _ in range(n_test):
        n, m = map(int, input().split(" "))    
        inputs = list(map(int, input().split(" ")))
        li_temp = []
        for i in range(n):
            row = [] 
            for j in range(m):
                row.append(inputs[i * m + j])
            li_temp.append(row)
        
        li_total.append(li_temp)
    
    return n_test, n, m, li_total

def down_top(li):
    n, m = len(li), len(li[0])
    
    comm = [[0] * m for _ in range(n)]
    for i in range(n):
        comm[i][-1] = li[i][-1]
    
    for j in reversed(range(m - 1)):
        for i in reversed(range(n)):
            for di, dj in move:
                i_tmp, j_tmp = i + di, j + dj
                if not (0 <= i_tmp < n and 0 <= j_tmp < m):
                    continue
                comm[i][j] = max(li[i][j] + comm[i + di][j + dj], comm[i][j])
    
    for _ in range(n):
        print(comm[_])
    return max([comm[i][0] for i in range(n)])

def main():
    n_test, n, m, li_total = get_inputs()
    
    for t in range(n_test):
        print(down_top(li_total[t]))

if __name__ == "__main__":
    main()
    
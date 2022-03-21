def get_input():
    N = int(input())
    li = [list(map(int, input().split(" "))) for _ in range(N)]

    return N, li

def dynamics(li, n):
    max_list = [0] * n
    
    for date in reversed(range(n)):
        time, pay = li[date]

        if date + time - 1 < n:
            max_list[date] = pay

        if  date + time < n:
            max_list[date] = max_list[date] + max(max_list[date + time:])
    
    #print(max_list)
    return max(max_list)

def main():
    N, li = get_input()
    max_value = dynamics(li, N)
    print(max_value)


if __name__ == "__main__":
    main()

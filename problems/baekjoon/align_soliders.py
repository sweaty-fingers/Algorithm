def get_input():
    N = int(input())
    li = list(map(int, input().split(" ")))

    return N, li

def dynamics(n, li):
    results = [1] * n

    for i in reversed(range(n - 1)):
        results_temp = [results[j] for j in range(i+1, n) if li[i] > li[j]]
        #print(f"{i} : {results_temp!r}")

        if results_temp:
            results[i] = results[i] + max(results_temp)
        
    #print(results)
    return n - max(results)


def main():
    n, li = get_input()
    print(dynamics(n, li))


if __name__ == "__main__":
    main()
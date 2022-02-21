def get_input():
    N, C = map(int, input().split(" "))
    
    li = [int(input()) for _ in range(N)]
    
    return C, li

def bisect(li, C):
    
    start = 1
    end = li[-1] - li[0]
    min_len = 0

    while start <= end:
        count = 1
        pre = li[0]
        mid = start + (end - start) // 2
        
        for i in range(1, len(li)):
            if li[i] - pre >= mid:

                count += 1
                pre = li[i]
            
        if count >= C:
            start = mid + 1
            min_len = mid 
        else:
            end = mid - 1

                
    return min_len
        
def main():
    C, li = get_input()
    li.sort()

    print(bisect(li, C))

if __name__ == "__main__":
    main()
import sys

def get_input():
    N = int(input())
    li = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    
    return li

def bisect_left(li):
    start = 0
    end = len(li) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if li[mid] == mid:
            return mid
        elif li[mid] > mid:
            end = mid - 1
        elif li[mid] < mid:
            start = mid + 1
    return -1

def main():
    li = get_input()
    answer = bisect_left(li)
    print(answer)

if __name__ == "__main__":
    main()
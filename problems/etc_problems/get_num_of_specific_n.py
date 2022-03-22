import sys
def get_input():
    N, x = map(int, input().split(" "))
    input_data = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    return input_data, x


def binary_search_left(li, target):
    start = 0 
    end = len(li) - 1
    mid = 0
    idx = -1
    while start <= end:
        mid = start + (end - start) // 2
        if li[mid] == target:
            idx = mid
            end = mid - 1
        elif li[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
    return idx


def binary_search_right(li, target):
    start = 0 
    end = len(li) - 1
    mid = 0
    idx = -1
    while start <= end:
        mid = start + (end - start) // 2
        if li[mid] == target:
            idx = mid
            start = mid + 1
        elif li[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return idx


def main():
    li, target = get_input()
    
    print(f"target: {target}")
    print((f"li: {li!r}"))
    idx_left = binary_search_left(li, target)
    idx_right = binary_search_right(li, target)
    
    if idx_left == -1 or idx_right == -1:
        print(f"{(idx_left + idx_right) // 2}")
    else:
        print(f"{idx_right - idx_left + 1}")
    
if __name__ == "__main__":
    main()
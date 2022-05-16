def get_input():
    
    N, C = map(int, input().split(" "))
    
    houses = [int(input()) for _ in range(N)]
    
     
    return N, C, houses

def bisec(houses):
    global N, C
    
    start = 1
    end = houses[-1] - houses[0]
    
    result = 0
    while start <= end:
        mid = start + (end - start) // 2
        count = 1
        prev = houses[0]
        
        for i in range(1, len(houses)):
            if houses[i] - prev >= mid:
                count += 1
                prev = houses[i]
            
        if count >= C:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
            
    return result
        

def main():
    global N 
    global C
    
    N, C, houses = get_input()
    houses.sort()
    print(bisec(houses))
    
    
if __name__ == "__main__":
    main()
    
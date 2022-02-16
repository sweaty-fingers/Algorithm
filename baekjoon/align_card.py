import heapq
def get_input():
    N = int(input())
    li = []
    for _ in range(N):
        li.append(int(input()))
        
    return li

def main():
    li = get_input()
    heapq.heapify(li)
    result = 0
    
    if len(li) == 1:
        print(result)
    else:
        while len(li) >= 2:
            sum_ = 0
            for _ in range(2):
                sum_ += heapq.heappop(li)
            
            result += sum_
            
            heapq.heappush(li, sum_)

        print(result)

if __name__ == "__main__":
    main()
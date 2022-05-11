import heapq

def get_input():
    n = int(input())
    cards = [int(input()) for _ in range(n)]
    
    return cards

def main():
    cards = get_input()
    heapq.heapify(cards)
    
    if len(cards) == 2:
        return sum(cards)
    
    n_compare = 0
    
    while len(cards) > 1:
        c = heapq.heappop(cards) + heapq.heappop(cards)
        n_compare += c
        
        heapq.heappush(cards, c)
    
    print(n_compare)


if __name__ == "__main__":
    main()
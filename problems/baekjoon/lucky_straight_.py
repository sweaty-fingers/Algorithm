def get_input():
    N = input()
    return N


def lucky_straight(N):
    
    len_half = len(N) // 2
    result = 0 
    for i, n in enumerate(N):
        if i < len_half:
            result += int(n)
        else:
            result -= int(n)
            
    
    if result == 0:
        return "LUCKY"

    else:
        return "READY"
    

def main():
    N = get_input()
    lucky_straight(N)
    print(lucky_straight(N))


if __name__ == "__main__":
    main()
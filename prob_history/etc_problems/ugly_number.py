def get_input():
    n = int(input())

    return n

def dynamics(n):
    indices = 1
    num = 2
    while True:
        if num % 2 == 0 or num % 3 ==0 or num % 5 == 0:
            indices += 1
        
        if indices == n:
            return num

        num += 1

def main():
    n = get_input()
    print(dynamics(n))


if __name__ == "__main__":
    main()
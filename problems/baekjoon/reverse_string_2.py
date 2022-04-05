def get_input():
    s = input()

    return s

def main():
    s = get_input()
    results = [0] * 2
    prev = int(s[0])
    results[prev] += 1
    
    for i in s[1:]:
        i = int(i)

        if i != prev:
            results[i] += 1
            prev = i 

    print(min(results))
if __name__ == "__main__":
    main()
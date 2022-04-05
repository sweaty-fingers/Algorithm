from typing import final


def get_input():
    return input()

def main():
    S = get_input()

    result = int(S[0])
    for s in S[1:]:
        s = int(s)
        if s <= 1 or result <= 1:
            result += s
        else:
            result *= s
    
    print(result)


if __name__ == "__main__":
    main()

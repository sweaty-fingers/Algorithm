if __name__ == "__main__":
    N = input()
    len_n = len(N)

    left_half = 0

    for i in N[:len_n//2]:
        left_half += int(i)

    right_half = 0
    for j in N[len_n//2:]:
        right_half = right_half + int(j)

    if left_half == right_half:
        print("LUCKY")
    else:
        print("READY")
        
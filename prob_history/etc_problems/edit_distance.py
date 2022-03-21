def get_input():
    txt_li = [input() for _ in range(2)]

    return txt_li[0], txt_li[1]


def dynamics(txt_from, txt_to):
    results = []
    len_row = len(txt_from)
    len_col = len(txt_to)
    for _ in range(len_row):
        results.append([0] * len_col)

    for i in range(len_row):
        results[i][0] = i
    for j in range(len_col):
        results[0][j] = j

    for i in range(1, len_row):
        for j in range(1, len_col):

            if txt_from[i] == txt_to[j]:
                results[i][j] = results[i-1][j-1]
            else:
                results[i][j] = 1 + min(results[i-1][j-1], results[i-1][j], results[i][j-1])
    
    for _ in range(len_row):
        print(f"{results[_]!r}")

    return results[-1][-1]



def main():
    txt_from, txt_to = get_input()
    txt_from = " " + txt_from
    txt_to = " " + txt_to

    print(f"txt_from: {txt_from}")
    print(f"txt_to: {txt_to}")

    print(dynamics(txt_from, txt_to))

if __name__ == "__main__":
    main()
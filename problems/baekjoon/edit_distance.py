def get_input():
    a = input()
    b = input()
    
    return a, b


def edit_distance(a, b):
    len_a = len(a)
    len_b = len(b)
    edit_map = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    for i in range(1, len_a + 1):
        edit_map[i][0] = i
    
    for i in range(1, len_b + 1):
        edit_map[0][i] = i
    
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                edit_map[i][j] = edit_map[i - 1][j - 1]
            else:
                edit_map[i][j] = 1 + min(edit_map[i][j - 1], edit_map[i - 1][j - 1], edit_map[i - 1][j])
        
    for i in range(len_a + 1):
        print(edit_map[i])
    
    print(edit_map[-1][-1])

def main():
    a, b = get_input()
    edit_distance(a, b)

if __name__ == "__main__":
    main()
    
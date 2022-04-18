def get_input():
    S = input()
    
    return S


def realign_string(S):
    
    s_list = []
    num = 0
    for s in S:
        if 65 <= ord(s) < 123:
            s_list.append(s)
            
        else:
            num += int(s)

    s_list.sort()
    
    return "".join(s_list) + str(num)

def main():
    S = get_input()
    print(realign_string(S))
    
    
if __name__ == "__main__":
    main()
def align(S):
    
    chr_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chr = []
    num = 0
    
    for s in S:
        if s in chr_list:
            chr.append(s)
        else:
            num += int(s)
    chr.sort()
    
    return "".join(chr) + str(num)
    

if __name__ == "__main__":
    
    S = input()
    result = align(S)
    print(result)
    
    
    
    
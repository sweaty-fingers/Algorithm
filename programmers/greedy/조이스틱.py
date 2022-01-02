def solution(name):
    
    ord_list = [ord(i) - ord('A') if ord(i) - ord('A') <= 13
                else 26 - (ord(i) - ord('A'))
                for i in name]
    
    cursor_full = len(ord_list) - 1
    
    if 0 not in ord_list:
        return sum(ord_list) + cursor_full
    
    zero_seq_temp = 0
    zero_seq_max = [0, 0]
    zero_seq = []
    
    for i in range(1, len(ord_list)):
        
        if ord_list[i] == 0:
            zero_seq_temp += 1
            
            zero_seq_max[0] = max(zero_seq_temp, zero_seq_max[0])
            
            if zero_seq_max[0] == zero_seq_temp:
                zero_seq_max[1] = i - zero_seq_temp + 1
        
        elif ord_list[i] != 0 and zero_seq_max[0] != 0:
            zero_seq.append(zero_seq_max[:])
            zero_seq_temp = 0
            
    if zero_seq_max not in zero_seq and zero_seq_max[0] != 0:
        zero_seq.append(zero_seq_max[:])
        
    cursor_right = 0
    cursor_left = 0
    cursor = cursor_full
    print(zero_seq)
    
    for zero_seq_max in zero_seq:
        s_max_zero_seq = zero_seq_max[1]
        e_max_zero_seq = zero_seq_max[1] + zero_seq_max[0] - 1

        cursor_right = max((s_max_zero_seq - 1) * 2 + len(ord_list) - (e_max_zero_seq + 1), 0)
        cursor_left = max((len(ord_list) - (e_max_zero_seq + 1)) * 2 + (s_max_zero_seq - 1), 0)
        
        cursor = min(cursor, cursor_right, cursor_left)
        
    return  sum(ord_list) + cursor
def solution(num_list):
    
    a = num_list[0]
    b = num_list[0]
    for i in range(len(num_list)-1):
        a *= num_list[i+1]
        b += num_list[i+1]

    b = b * b

    if a < b:
        return 1
    elif a > b:
        return 0
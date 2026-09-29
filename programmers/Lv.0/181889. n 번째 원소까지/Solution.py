def solution(num_list, n):
    a = []
    x = 0
    for i in num_list:
        a.append(i)
        x += 1
        if x == n:
            break
    return a
def solution(strArr):
    new = []
    for i,j in enumerate(strArr):
        if i % 2:
            new.append(j.upper())
        else:
            new.append(j.lower())
    return new

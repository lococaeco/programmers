def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    x = myString.find(pat) + 1
    if x:
        return 1
    else:
        return 0
def solution(rny_string):
    origin = ""
    for i in rny_string:
        if i == "m":
            origin += "rn"
        else:
            origin += i

    return origin
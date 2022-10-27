def solution(babbling):
    baby_say = ["aya", "ye", "woo", "ma",
               "00","11","22","33"]
    answer = 0
    for bab in babbling:
        for i in range(4):
            bab = bab.replace(baby_say[i], str(i))
        for i in range(4,8):
            bab = bab.replace(baby_say[i], "a")
        if bab.isdigit(): answer += 1
    return answer
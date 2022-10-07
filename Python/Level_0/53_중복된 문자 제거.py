def solution(my_string):
    li = [1]*53
    answer = ''
    for i in my_string:
        if i == " ":
            n = 52
        elif i.isupper():
            n = ord(i) - ord("A") + 26
        else:
            n = ord(i) - ord("a")
        if li[n]:
            answer += i
            li[n] = 0
    return answer
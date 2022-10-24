def solution(n, words):
    count = 1
    man = 1
    last = words[0][0]
    dic = dict()
    for word in words:
        if word in dic or last != word[0]:
            return [man, count]
        dic[word] = 1
        man += 1
        last = word[-1]
        if man > n:
            man = 1
            count += 1
    return [0,0]
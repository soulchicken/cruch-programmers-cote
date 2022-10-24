def solution(n):
    one = bin(n).count('1')
    while 1:
        n += 1
        if bin(n).count('1') == one:
            return n
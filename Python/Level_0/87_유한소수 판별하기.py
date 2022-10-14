def solution(a, b):
    while a != 1:
        for i in range(2,a+1):
            if not a % i + b % i:
                a //= i
                b //= i
                break
        if i == a: break
    while not b % 2:b //= 2
    while not b % 5:b //= 5
    
    if b == 1:return 1
    return 2
def solution(sides):
    a,b,c = sorted(sides)
    return 2 if a+b <= c else 1
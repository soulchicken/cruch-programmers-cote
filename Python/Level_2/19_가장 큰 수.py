def solution(numbers):
    def f(s): return str(s)*6
    def g(s): return s[:len(s)//6]
    return ''.join(map(g,sorted(list(map(f,numbers)))[::-1])).lstrip('0') or '0'
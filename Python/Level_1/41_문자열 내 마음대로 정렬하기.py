def solution(strings, n):
    return [s[1:]for s in sorted(s[n]+s for s in strings)]
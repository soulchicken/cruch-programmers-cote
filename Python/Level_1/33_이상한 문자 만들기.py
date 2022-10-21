def solution(s):
    return ' '.join(''.join(a.lower() if i%2 else a.upper() for i,a in enumerate(w)) for w in s.split())
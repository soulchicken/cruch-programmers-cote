def solution(s, n):
    return ''.join(' ' if i==' ' else chr((ord(i) - ord('A') + n)%26 + ord('A')) if i.isupper() else chr((ord(i) - ord('a') + n)%26 + ord('a')) for i in s)
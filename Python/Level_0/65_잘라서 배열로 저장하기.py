def solution(my_str, n):
    return [my_str[i*n:i*n+n] for i in range(1 + len(my_str)//n  if len(my_str)%n else len(my_str)//n )]
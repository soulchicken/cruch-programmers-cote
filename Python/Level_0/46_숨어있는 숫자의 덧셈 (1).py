def solution(my_string):
    return sum(int(i) if i.isdigit() else 0  for i in my_string)
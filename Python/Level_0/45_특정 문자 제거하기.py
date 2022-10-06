def solution(my_string, letter):
    return ''.join([i if i != letter else "" for i in my_string])
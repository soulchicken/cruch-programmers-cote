def solution(my_string):
    return my_string.translate(str.maketrans('aeiou', '11111')).replace('1','')
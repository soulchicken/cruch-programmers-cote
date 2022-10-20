def solution(price, money, count):
    return max(0,price*(1+count)*count//2 - money)
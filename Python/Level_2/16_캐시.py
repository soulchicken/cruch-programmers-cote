def solution(cacheSize, cities):
    from collections import deque
    answer = 0
    cache = deque()
    count = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if cacheSize:
                if cacheSize and count == cacheSize:
                    cache.popleft()
                    count -= 1
                count += 1
                cache.append(city)
    return answer
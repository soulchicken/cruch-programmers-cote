def solution(n, m, section):
    answer = 1
    val = section.pop()
    while section:
        if val - m < section[-1]:
            section.pop()
        else:
            answer += 1
            val = section.pop()
    return answer
def solution(id_list, report, k):
    kill = dict()
    repo = dict()
    for i in id_list:
        kill[i] = []
        repo[i] = 0
    for r in set(report):
        a,b = r.split()
        kill[b].append(a)
    for i in id_list:
        if len(kill[i]) >= k:
            for j in kill[i]:
                repo[j] += 1
    return [repo[i] for i in id_list]
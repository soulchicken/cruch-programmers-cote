def solution(bridge_length, weight, truck_weights):
    from collections import deque
    bridge = deque([0]*bridge_length)
    total_weight = 0
    TOTAL_TRUCK = sum(truck_weights)
    bridge_weight = 0
    answer = 0
    while TOTAL_TRUCK != total_weight:
        answer += 1
        pop_truck = bridge.pop()
        total_weight += pop_truck
        bridge_weight -= pop_truck
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.appendleft(truck)
            bridge_weight += truck
        else:
            bridge.appendleft(0)
    return answer

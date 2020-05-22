from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    cross = deque([])
    crossed = []
    
    t = 0
    while truck_weights:
        if len(cross) == bridge_length:
            cross.popleft()
        if sum(cross)+truck_weights[0] <= weight:
            cross.append(truck_weights.popleft())
            t += 1
        else:
            while len(cross) < bridge_length:
                cross.append(0)
                t += 1

    return t+bridge_length
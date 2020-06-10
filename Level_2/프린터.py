from collections import deque

def solution(priorities, location):
    answer = 1
    priorities = deque(priorities)
    order = deque(range(len(priorities)))
    
    while True:
        maxV = max(priorities)
        length = len(priorities)
        for _ in range(length):
            p = priorities.popleft()
            o = order.popleft()
            if p == maxV:
                if o == location:
                    return answer
                answer += 1
                break
            else:
                priorities.append(p)
                order.append(o)
    
    return answer
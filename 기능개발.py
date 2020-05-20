def solution(progresses, speeds):
    answer = []

    distribute = []

    for i in range(len(progresses)-1,-1,-1):
        day = (100-progresses[i])//speeds[i]+1 if (100-progresses[i])%speeds[i] else (100-progresses[i])//speeds[i]
        distribute.append(day)

    while distribute:
        criteria = distribute.pop(); cnt = 1
        if not distribute:
            answer.append(cnt)
        else:
            while distribute and distribute[-1] <= criteria:
                distribute.pop()
                cnt += 1
            answer.append(cnt)

    return answer
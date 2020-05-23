def solution(prices):
    answer = []
    for i in range(len(prices)):
        period = 0
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                period += 1
                break
            else:
                period += 1
        answer.append(period)
    return answer
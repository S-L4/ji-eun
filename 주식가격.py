def solution(prices):
    answer = []
    for i in range(len(prices)):
        period = 0
        for j in range(i+1,len(prices)):
            period += 1
            if prices[i] > prices[j]:
                break
        answer.append(period)
    return answer
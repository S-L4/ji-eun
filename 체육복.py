def solution(n, lost, reserve):
    answer = n-len(lost)
    reserve_check = [False]*(n+1)
    lost_check = [False]*(n+1)
    
    for i in reserve:
        if i in lost:
            reserve_check[i] = True
            lost_check[i] = True
            answer += 1

    for i in lost:
        if not lost_check[i]:
            for j in reserve:
                if not reserve_check[j] and abs(i-j) == 1:
                    reserve_check[j] = True
                    lost_check[i] = True
                    answer += 1
                    break

    return answer
def solution(heights):
    answer = [0]*(len(heights)+1)
    while heights:
        height = heights.pop()
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > height:
                answer[len(heights)] = i
                break
    return answer[1:]
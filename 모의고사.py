def solution(answers):
    answer = []
    math_giveup1 = [1,2,3,4,5]
    math_giveup2 = [2,1,2,3,2,4,2,5]
    math_giveup3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0]*3
    
    for i in range(len(answers)):
        if answers[i] == math_giveup1[i%5]:
            scores[0] += 1
        if answers[i] == math_giveup2[i%8]:
            scores[1] += 1
        if answers[i] == math_giveup3[i%10]:
            scores[2] += 1
    
    max_giveup = 0
    for i in range(3):
        if scores[i] > max_giveup:
            max_giveup = scores[i]
    
    for i in range(3):
        if scores[i] == max_giveup:
            answer.append(i+1)
        
    return answer
def solution(arrangement):
    answer = 0; laser = []
    for i in range(len(arrangement)-1,-1,-1):
        if arrangement[i] == ')':
            laser.append(0)
            flag = True
        else:
            if flag:
                if laser:
                    laser.pop()
                    if laser:
                        laser[-1] += 1
            else:
                num = laser.pop()
                answer += num + 1
                if laser:
                    laser[-1] += num
            flag = False
              
    return answer


# # 다른 사람의 풀이
# def solution(arrangement):
#     answer = 0
#     sticks = 0
#     rasor_to_zero = arrangement.replace('()','0')

#     for i in rasor_to_zero:
#         if i == '(':
#             sticks += 1
#         elif i =='0' :
#             answer += sticks
#         else :
#             sticks -= 1
#             answer += 1

#     return answer
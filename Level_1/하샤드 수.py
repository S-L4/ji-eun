def solution(x):
    sum_x = sum([int(x) for x in str(x)])
    return False if x%sum_x else True
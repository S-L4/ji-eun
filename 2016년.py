def solution(a, b):
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    num = b
    for i in range(1,a):
        num += months[i]

    return days[num%7]
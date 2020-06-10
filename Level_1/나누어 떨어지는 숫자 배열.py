def solution(arr, divisor):
    answer = []
    for element in arr:
        if not element%divisor:
            answer.append(element)

    return sorted(answer) if answer else [-1]
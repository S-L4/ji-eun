def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        flag = False
        visited = []
        for s in skill:
            comp_idx = len(skill_tree)
            visited.append(s)
            for i in range(len(skill_tree)):
                if s == skill_tree[i]:
                    comp_idx = i
                    break
            for j in range(len(skill_tree)):
                if skill_tree[j] in visited:
                    continue
                else:
                    if skill_tree[j] in skill:
                        if j < comp_idx:
                            flag = True
                            break
            if flag:
                break
        else:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
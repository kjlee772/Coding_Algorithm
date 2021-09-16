rule_one = [1,2,3,4,5]
rule_two = [2,1,2,3,2,4,2,5]
rule_thr = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    answer = []
    
    count = [0,0,0]
    
    for i in range(len(answers)):
        if rule_one[i%5] - answers[i] == 0:
            count[0] += 1
        if rule_two[i%8] - answers[i] == 0:
            count[1] += 1
        if rule_thr[i%10] - answers[i] == 0:
            count[2] += 1
    
    for i in range(len(count)):
        if count[i] == max(count):
            answer.append(i+1)
    
    return answer
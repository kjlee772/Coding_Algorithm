from collections import Counter

def solution(participant, completion):
    answer = ''
    
    for i in participant:
        if i not in completion:
            print(i)
            
            
    
    
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# for i in completion:
#     if i in participant:
#         participant.remove(i)
print(list(Counter(participant)-Counter(completion))[0])
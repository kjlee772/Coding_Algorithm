import itertools
import math

def prime(input):
    if input < 2:
        return False
    for i in range(2, int(math.sqrt(input))+1):
        if input % i == 0:
            return False
    return True

def solution(numbers):    
    answer = 0
    
    split_num = []
    for i in numbers:
        split_num.append(i)
    split_num.sort()
    
    make_num = []
    for i in range(len(numbers)):
        temp = itertools.permutations(split_num, i+1)
        for i in temp:
            make_num.append(int("".join(i)))
    
    for i in set(make_num):
        if prime(i):
            answer += 1

    return answer
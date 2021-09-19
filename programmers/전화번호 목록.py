def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        key = phone_book.pop(i)

        for item in phone_book:
            if key in item:
                answer = False

        phone_book.insert(i,key)
    
    return answer
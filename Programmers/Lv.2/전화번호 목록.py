def solution(phone_book):
    book = []
    for i in phone_book:
        book.append((i, len(i)))
        
    book.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(book)-1):
        if book[i+1][0].startswith(book[i][0]):
            return False
        
    # phone_book.sort(key=len)
    # for i in range(len(phone_book)):
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[j].startswith(phone_book[i]):
    #             return False

    return True
def solution(s):
    # s = 'ghe  aef  a asdfe  asdf   eff'
    print(s.split(' '))
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


# def solution(s):
#     answer = ''
#     count = 0
#     for i in list(s):
#         if i != ' ':
#             answer += i.upper() if count % 2 == 0 else i.lower()  ## change
#             count += 1
#         else:
#             answer += i
#             count = 0
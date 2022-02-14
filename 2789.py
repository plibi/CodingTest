word = input()
ban = 'CAMBRIDGE'

for i in ban:
    if i in word:
        word = word.replace(i, '')

print(word)

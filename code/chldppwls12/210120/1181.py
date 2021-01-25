words = []
for i in range(int(input())):
    words.append(input())

words = list(set(words))

sort_words = []

for j in words:
    sort_words.append((len(j), j))

sort_words.sort()

for len_word, word in sort_words:
    print(word)
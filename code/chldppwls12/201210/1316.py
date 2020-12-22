n = int(input())

for i in range(n):
    flag = True
    word = input()
    word_len = len(word)
    for j in range(word_len-1):
        if word[j] != word[j+1]:
            next_word = word[j+1:]
            if word[j] in next_word:
                flag = False
                break
    if flag == False:
        n = n-1
print(n)
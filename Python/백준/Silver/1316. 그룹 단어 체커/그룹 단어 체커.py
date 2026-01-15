count = 0
for _ in range(int(input())):
    word = input()
    error = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if word[i] in new_word:
                error += 1
                break
    if error == 0:
        count += 1

print(count)

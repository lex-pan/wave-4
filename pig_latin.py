vowels = ["a", "i", "e", "o", "u"]
newSentence = []
sentence = input().split()

for word in sentence:
    position = 0
    while position < len(word):
        if word[position] in vowels:
            if position == 0:
                newSentence.append(word + "way")
            else:
                newSentence.append(word[position:] + word[0:position] + "ay")
            break
        position += 1

print('  '.join(newSentence))


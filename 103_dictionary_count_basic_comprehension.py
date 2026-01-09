sentence = "Python is fun,amazing! is not it? Python is great."
count = {}
for char in ",.!?":
    sentence = sentence.replace(char, " ")
for word in sentence.lower().split():
    count[word] = count.get(word, 0) + 1
print(count)

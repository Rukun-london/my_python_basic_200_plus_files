# Asks the user to enter a sentence
# Converts it to lowercase
# Counts how many times each word appears
# Prints the dictionary
# Example:
# Input: Python is fun and Python is powerful/Python, is fun! Python?
# Output: {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}
sentence= input("Enter a sentence: ")
count={}
for char in ",.!?":
    sentence = sentence.replace(char, " ")
sentence=sentence.lower()
words=sentence.split()
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)



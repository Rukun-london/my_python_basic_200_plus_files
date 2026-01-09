# counting word from a file
count = {}

with open("sample.txt", "r") as file:
    for line in file:
        line = line.lower()
        for char in ",.?!":
            line =line.replace(char,"")
        print("processing line: ",line)
        words = line.split()
        for word in words:
            count[word]=count.get(word,0)+1
print(count)



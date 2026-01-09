# create a new file from an existing file
count = {}

with open("sample.txt", "r") as file:
    for line in file:
        line = line.lower()
        for char in ",.?!":
            line = line.replace(char, "")
        print("processing line: ", line.strip())
        words = line.split()
        for word in words:
            count[word] = count.get(word, 0) + 1
print(count)
with open("result.txt", "w") as file:
    for word, frequency in count.items():
        file.write(f"{word} : {frequency}\n")

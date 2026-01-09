# count lines of a file
with open("result.txt", "r") as file:
    lines=file.readlines()
for line in lines:
    print(line.strip())
print("Total number of lines: ", len(lines))

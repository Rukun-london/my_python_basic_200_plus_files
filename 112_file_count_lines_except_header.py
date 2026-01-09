# count lines except header
count=0
with open("result.txt", "r") as file:
    lines = file.readlines()
    for line in lines[3:]:
        print(line.strip())
        count+=1
print(f"There are {count} names in result.txt")
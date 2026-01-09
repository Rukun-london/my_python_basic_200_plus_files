#remove duplicate
count=0
with open("result.txt", "r") as file:
    lines = file.readlines()
    names=set(line.strip() for line in lines[3:])
    for name in names:
        print(name)
        count+=1
print(f"There are {count} names in result.txt")
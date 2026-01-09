# use def count_names(): remove duplicate
def count_names():
    with open("result.txt", "r") as file:
        lines = file.readlines()
        names = set(line.strip() for line in lines[3:])
    return len(names)

print(f"There are {count_names()} names in result.txt")

def count_names():
    with open("result.txt", "r") as file:
        lines = file.readlines()
        unique_names = set()

        for line in lines[3:]:
            name = line.strip()
            if name:
                unique_names.add(name)

    return len(unique_names)

print("There are", count_names(), "unique names in result.txt")
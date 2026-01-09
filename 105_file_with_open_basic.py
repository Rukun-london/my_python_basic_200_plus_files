# file with open function, the file close itself by default
with open("sample.txt", "r") as file:
    count={}
    for line in file:
        print(line.strip())
        # print(line) after evey iteration there will be a new line (/n),
        # mean double gap for the output of our file sample.txt
        #gap between the line will be gone

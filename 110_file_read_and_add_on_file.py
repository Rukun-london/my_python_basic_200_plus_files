# read and add on a file
name = input("enter your name: ")
with open("result.txt", "a") as file:
    # file.write("\n"+name) or
    file.write(f"\n{name}")
with open("result.txt", "r") as file:
    content = file.read()
    print(content)

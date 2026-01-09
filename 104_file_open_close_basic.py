#if we open a file, we must need to close it
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

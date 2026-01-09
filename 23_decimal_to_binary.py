#decimal to binary
count=int(input("How many numbers do you want to transform to binary? "))
i=0
while(i<=count):
    num=int(input("Enter a number: "))
    binary=bin(num)
    print(f" the binary of {num} is : {binary[2:]}")
    i=i+1
#bianry to decimal
count=int(input("How many numbers do you want to transform into decimal:  "))

i=1
while(i<=count):
    binary = (input("Enter a binary number consist of 0 and 1 : "))
    decimal = int(binary,2)
    print(f" The decimal value of the binary number {binary} is :{decimal}")
    i=i+1
    



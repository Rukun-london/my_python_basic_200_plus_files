# Construct a range of perfect numbers
#perfecr numbers are made by adding up their factors
# 2
def is_perfect(n):
    if n<2:
        return False
    divisors=[i for i in range(1,n//2+1) if n%i==0 ]
    return sum(divisors)==n
num_range=int(input("Enter a number for a range: "))
perfect_numbers=[]
spinners=['|','/','-','\\']
for n in range(1,num_range):
    # for s in spinners:
    #     sys.stdout.write(f"\rChecking {n}/{num_range}......... {s}")
    #     sys.stdout.flush()
    #     time.sleep(.1)
    if is_perfect(n):
        perfect_numbers.append(n)

print(f"\nThe perfect numbers are : ",perfect_numbers)
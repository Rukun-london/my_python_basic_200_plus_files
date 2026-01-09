#61_prime_factors_of_a_number
def prime_factors(n):
    factors=[]
    i=2
    while i*i<=n:
        if n%i==0:
            n=n//i
            factors.append(i)
        else:
            i+=1
    if i*i>n:
        factors.append(n)
    return factors
count=int(input("how many times do you want to check: "))
turn=1
for turn in range(count):
    num=int(input("Enter a number for prime factors: "))
    print(f"Prime factors for {num} : {prime_factors(num)}")

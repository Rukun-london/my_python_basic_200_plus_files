number = int(input("Enter a number: "))

# Handle special cases
if number <= 1:
    print("It is not a prime number!")
else:
    is_prime = True
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("It is a prime number!")
    else:
        print("It is not a prime number!")
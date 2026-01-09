def is_prime(num: int) -> bool:
    # Handle edge cases
    if num <= 1:
        return False
    if num == 2:
        return True

    # Check divisibility from 2 up to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main program
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number ✅")
else:
    print(f"{number} is not a prime number ❌")
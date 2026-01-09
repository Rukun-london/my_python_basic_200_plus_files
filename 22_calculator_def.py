def calculator(a,b,op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b==0:
            raise ValueError("Cannot divide by zero")
        return a/b
    else:
        raise ValueError("Invalid operator")
a=int(input("What is your first number?: "))
op=str(input("What is your operator? Enter (+-*/): "))
b=int(input("What is your second number?: "))
print(f" Operation {a} {op} {b} = {calculator(a,b,op)}")
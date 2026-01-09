#find the roots of a quadratic equation
#x=(-b+_(b**2-4*a*c)**1/2)/2a
import cmath
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
d=cmath.sqrt(b*b-4*a*c)
root1=(-b+d)/(2*a)
root2=(-b-d)/(2*a)
print(f"the roots are {root1} and {root2}")
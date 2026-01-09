
while True:
    year = int(input(" Enter a year: "))
    if year % 400 == 0 :
        print(" this is a leap year")
        break
    elif year % 100 == 0:
        print(" this is not  a leap year")
    elif year % 4 == 0 :
        print(" this is a leap year")
        break
    else:
        print(" this is not a leap year")

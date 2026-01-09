
def is_leap_year( year : int ) -> bool :
    if year % 400 == 0 :
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0 :
        return True
    else:
        return False

while True:
    year = int(input(" Enter a year: "))
    if is_leap_year(year):
        print( year, "is a leap year")
        break
    else:
        print(year, " is not a leap year. Try again !")
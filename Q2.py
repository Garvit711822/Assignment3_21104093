year = int(input("Input a year: "))
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
elif((year>2025)|(year<1800)):
    print("Error")
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
elif month in (4,6,9,11):
    month_length = 30
else:
    print("error!")

day = int(input("Input a day [1-31]: "))
if day < month_length:
    day += 1
    print("The next date is",day,"-",month,"-",year)
elif day==month_length:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
    print("The next date is",day,"-",month,"-",year)
else:
    print("Error! Please enter valid input.")

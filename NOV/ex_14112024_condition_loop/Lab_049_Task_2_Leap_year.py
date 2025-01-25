'''
This extra leap day occurs in each year that is a multiple of 4,
except for years evenly divisible by 100 but not by 400.
'''

year=int(input("Enter the year\n"))
if year%4==0 and year%100==0 and year%400==0 :
    print("Year is leap year")
#elif year%100==0 and year%400==0:
    #print("Year is leap year")
else:
    print("Year is not a leap year")

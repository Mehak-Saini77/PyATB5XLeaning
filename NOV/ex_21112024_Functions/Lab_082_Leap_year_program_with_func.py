
year= int(input("Enter the year\n"))

def leapyear(year):
   if (year%4==0 and year%100!=0 or year%400==0):
       print("Year is leap year")

   else:
       print("Year is not leap year")

leapyear(year)
# Area of circle
import math
#pi *r*2

pi=3.14

Radius =float(input("Enter the Radius\n"))
area= pi*(Radius**2)
print(f"Area of circle -->{area:.2f}")
print(math.pi)
area2 =math.pi*math.pow(Radius,2)
print(f"Area of circle is -->{area2}")

# one liner code
print(3.14*(float(input("Enter the Radius\n"))**2))
import math

def power(num):
    return math.pow(num,2)

r1=power(3)
print(r1)

r2=lambda : math.pow(int(input("Enter the number\n")),2)

print(r2())
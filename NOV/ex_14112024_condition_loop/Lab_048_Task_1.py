'''
Write a program that classifies a triangle based on its side lengths.
Given three input values representation the length of the sides, determine if the triangles is equilaterals
 (All sides are equal)isosceles (exactly two sides are equal),or scalene(No sides are equals.)

'''

val1= float(input("Enter the value 1\n"))
val2= float(input("Enter the value 2\n"))
val3= float(input("Enter the value 3\n"))

if val1>0 and val2>0 and val3>0:
          if val1==val2==val3:
           print("triangles is equilaterals")
          elif val1==val2 or val2==val3 or val1==val3 :
           print("triangles is isosceles")
          else:
            print("triangles is scalene")

else:
        print("Invalid length")
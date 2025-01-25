# Create a program of sum of the three number from the user input ,
# if user doesn't enter any number,Use default as 100,200,300
a1=int(input("Enter the number 1=\n"))
b1=int(input("Enter the number 2=\n"))
c1=int(input("Enter the number 3=\n"))

def sum_three(a=100,b=200,c=300):
    return(a+b+c)

result=sum_three(a1,b1,c1)
print(f"Sum of the three numbers,{result}")
result2=sum_three()
print(f"witout user input Sum of the three numbers,{result2}")




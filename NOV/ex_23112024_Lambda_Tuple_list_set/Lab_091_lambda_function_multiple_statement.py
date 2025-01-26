# Write a program of even and odd number

def find_even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

    return(num)

result=find_even_odd(6)
num=int(input("Enter the number\n"))
r1=lambda num:"Even" if num %2== 0 else "Odd"

print(r1(num))
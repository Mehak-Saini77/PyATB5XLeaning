
#Can't return -->No return type
def greet():
    print("Hello Mehak")
greet()

# No return type with Argument

def func1(name):
 print("Hello,",(name))
func1("Mehak")

#No return type with default argument
def func2(Name="Savi"):
 print("Hello,",Name.upper())
func2()

 #No return type with multiple argument

def func3(name1="A",name2="B"):
 print("Hello,",name1,name2)
func3(name2="Saini")

#Argument with return type:
def sum(a,b):
    return(a+b)
result= sum(56,10)
print(f"Sum of two number is-->{result}")

# 2 usage case
def sum_default(a=10,b=20):
    return(a+b)
result= sum_default(20,20)
print(f"Sum of two number is-->{result}")
# 3 usage case
def sum_default1(a=10,b=20):
    return(a+b)
result= sum_default1()
print(f"Sum of two number is-->{result}")



#Function inside function

def hello():
    print("Hello world !!")


def hi():
    print("Hi i am inside the function")
    hello()

hi()
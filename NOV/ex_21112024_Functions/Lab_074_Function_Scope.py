pb_Global_b =12 # Global varible

# Case usage
def my_function():
    pb_a=10 # Local variable which can't be used out side the function
    print(pb_a)
    print(pb_Global_b)
print(pb_Global_b)
# print(pb_a) -->NameError: name 'pb_a' is not defined

my_function()
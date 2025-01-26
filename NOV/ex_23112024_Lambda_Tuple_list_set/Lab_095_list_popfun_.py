#The pop() method is used to remove an element from a list at a specified index and return that element.
# If no index is provided, it will remove and return the last element by default.
# This method is particularly useful when we need to manipulate a list dynamically,
# as it directly modifies the original list

squares=[1,4,5,6,8,23,90,9]
print(squares)
print(squares.pop())
print(squares)
print(squares.pop(4))
print(squares)

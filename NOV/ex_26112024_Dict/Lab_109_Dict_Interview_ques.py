#Function that returns the max value from the dictionary
#{"a":34,"b":39,"c":100}

def max_value(dictionary):
    return max(dictionary.values())

print(max_value({"a":34,"b":39,"c":100}))
print("***********************Min function***********************")
def min_value(dictionary):
    return min(dictionary.values()) # values function give list of all the value

print(min_value({"a":34,"b":39,"c":100}))
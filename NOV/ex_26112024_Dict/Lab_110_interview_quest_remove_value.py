# Remove duplicate values from the dictionary

my_dict = {"a": 4, "b": 3, "c": 1, "d": 4}
# output:{"a":4,"b":3,"c":1}

unique_value = set()
result = {}
for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

print(result)

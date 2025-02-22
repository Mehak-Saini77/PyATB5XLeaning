from html.parser import charref


def first_non_repeat(string):
    for char in string:
        if string.count(char) == 1:
            return char
    else:
        return None


print(first_non_repeat("swiss"))
print(first_non_repeat("look"))
print(first_non_repeat("dada"))



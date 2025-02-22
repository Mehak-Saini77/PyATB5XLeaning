input_string="hello,world"
#a,e,i,o,u
#vowel=
vowel="aeiou"
vowel_count=0
result=dict()

for char in input_string:
    if char in vowel:
        vowel_count=vowel_count+1


print(vowel_count)

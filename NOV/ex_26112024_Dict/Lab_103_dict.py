#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#As of Python version 3.7, dictionaries are ordered. In Python 3.6
# and earlier, dictionaries are unordered.

my_dict={
    "name":"Mehak",
    "age":24,
    "role":"Software tester",
    "Experience":2.5
}
print(my_dict)
print(my_dict["age"])
my_dict["role"]="Automation tester"

print(my_dict)
print("**************************************************************************************")
del my_dict["age"]

print(my_dict)

print("**************************************************************************************")

#iterate the key and value
for key,value in my_dict.items():
    print(key,"-->",value)

print("**********************Check key is present or not in dic**************************************************************************************")
#ckeing
print("age"in my_dict)
print("name"in my_dict)

#dictionary menthod

#get()
#keys()
#values()
#items()update()
#pop()
clear()




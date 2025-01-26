#List -->collection of items. These items can be of any data type,
# including integers, floats, strings, and even other lists.
# here duplicate items are allowed
# here we can use different data types

my_list=[1,2,3,4,5]# same type of data type (integers)
my_list2=[1,2,2.3,3.14,"Mehak",True]

print(my_list)
print(my_list2)
print(type(my_list2))
print(len(my_list))
print(my_list2[0])
print(my_list2[1])
print(my_list2[2])
print(my_list2[3])
print(my_list2[4])
print(my_list2[5])
#print(my_list2[6]) #IndexError: list index out of range

print("```````````````````````````````````````````````````````````````````````")
print("Reassign the value")
my_list2[3]="Saini"
my_list2[4]="Chirag"
print(my_list2)

print("[",end="")
for i in my_list:
    print(f"{i}",end=",")

print("]",end="")
print("")
for i in range(1,5):
     print(i)

print(type(range(1,2))) # range also return list



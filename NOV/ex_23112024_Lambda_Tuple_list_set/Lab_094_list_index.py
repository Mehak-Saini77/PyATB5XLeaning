from operator import index

my_list=[1,2,3,4]

#Indexing
print("Element at the index 0-",my_list[0])
print("Element at the index 1-",my_list[1])
print("Element at the index 2-",my_list[2])
print("Element at the index 3-",my_list[3])

print(len(my_list))

#append function --> append()
 # add the item in the end of the list
my_list.append(5)
my_list.append(8)
print(my_list)
print("***********************************************************************")

 # extend()- append  a new list
my_list.extend([3,9,6,10])
print(my_list)
print("***********************************************************************")
#insert
my_list.insert(1,9)
print(my_list)
print("***********************************************************************")

my_list.insert(3,8)
print(my_list)
print("***********************************************************************")
my_list[7]="7"
#Remove()
my_list.remove(2)
print(my_list)
print("***********************************************************************")
#Copy list
my_copy_list=my_list.copy()
print(my_copy_list)
print("***********************old list ************************************************")

my_copy_list[3]=2
my_copy_list[4]=34
print(my_list)
print(my_copy_list)
#sorting of copy list
print("***********************New list ************************************************")

new_list=[1,5,7,9,6,89]
new_list.extend([3,6,9,52,8])
print(new_list)
print("*********************** sort New list ************************************************")
new_list.sort()
print(new_list)
print("*********************** reverse New list ************************************************")
new_list.reverse()
print(new_list)

print("*********************** fruit New list ************************************************")
fruit_list=["Mango","Orange","Guava","Apple","Pineapple","Sopta","Grapes"]
fruit_list.sort(key=lambda x:x[0])
print(fruit_list)




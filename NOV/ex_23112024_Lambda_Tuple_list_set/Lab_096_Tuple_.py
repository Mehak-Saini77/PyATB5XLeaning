# Tuple is also collection of item
# tuple is immutable means we can't change the value
#syntax-->()

my_tuple=(1,4,6,8,5,9)
print(my_tuple)
# if we want to change the tuple value
#my_tuple[4]=6 #'tuple' object does not support item assignment
print(my_tuple)
shopping_item=["Bread","Butter","Milk","Jam"]
print(shopping_item)
shopping_item[3]="Soap"
print(shopping_item)

print("-----------Real example------------------")
tuple_link=("runbook.com","mysite.com")
print(tuple_link)
print("-----------type conversion of tuple to list ------------------")

my_api_list=list(tuple_link)
print(my_api_list)
my_api_list[1]="testguru.com"
print(my_api_list)

#real case ,where we use tuple ,so in case of url ,we know ,urls are not changeable
API_URLs=("https://courses.thetestingacademy.com/","https://www.bing.com/","https://www.geeksforgeeks.org/")
for i in API_URLs:
    print(i)

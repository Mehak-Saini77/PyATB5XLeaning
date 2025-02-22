#Dictornary from two list


keys=["name","role","experience"]
values=["Aman","Tester","2","5"]
my_dict_1=dict(zip(keys,values))
print(my_dict_1)


#merge two dict

dict1={"a":1,"b":2}
dict2={"c":6,"d":4}

merge_dict=dict1|dict2
print(merge_dict)

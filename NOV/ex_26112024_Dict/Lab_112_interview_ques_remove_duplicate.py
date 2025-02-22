#   Remove duplicates from this list

my_list={2,3,4,6,8,5,6,9,6}

def remove_dup(list):
    unique_list=set(my_list)
    return unique_list


print(remove_dup(my_list))
student_info_1 = {
    "name": "Chirag",
    "age": 24,
    "course": "cyber security program ",
    "Duration": 2,
    "Address":
        {
            "home_address": "Brampton,Canada",
            "Work_address": "Naigra fall"
        }
}

student_info_2 = {
    "name": "Mehak",
    "age": 25,
    "course": "cyber security program ",
    "Duration": 2,
    "Address":
        {
            "home_address": "Brampton,Canada",
            "Work_address": "Naigra fall"
        }
}
student_info_3 = {
    "name": "Abhi",
    "age": 23,
    "course": "cyber security program ",
    "Duration": 2,
    "Address":
        {
            "home_address": "Topra khurd",
            "Work_address": "Yamuna nagar"
        }
}

student_list = [student_info_1,student_info_2,student_info_3]
print(student_list)

print(student_list[0])
print(student_list[1])
print(student_list[1]["name"])
print(student_list[0]["name"])
print(student_list[1]["age"])
print(student_list[0]["age"])
print(student_list[1]["age"])
print(student_list[1]["Address"])
print(student_list[1]["Address"]["Work_address"])
print(student_list[2]["Address"]["Work_address"])
print(student_info_3["Address"])







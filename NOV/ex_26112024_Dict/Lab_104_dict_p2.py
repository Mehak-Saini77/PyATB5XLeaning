student_info={
"name":"Chirag",
    "age":24,
    "course":"cyber security program ",
    "Duration":2,
    "Address":"Brampton"

}
print(student_info["name"])
print(student_info["age"])
student_info["age"]=26
print(student_info)

#Another way for declare the dictionary

student_info_2= dict(name="Mehak",Age="25",address="Hyderabad")
print(student_info_2)

# dict within dict

student_info_1={
"name":"Chirag",
    "age":24,
    "course":"cyber security program ",
    "Duration":2,
    "Address":
    {
      "home_address":"Brampton,Canada",
        "Work address":"Naigra fall"
    }
}
print(student_info_1)

j=tuple()# we are create empty tuple by using tuple() function
print(j)

# type conversion of list to tuple
t1=tuple(["Mehak","Saini","Chirag","Abhi","Ram"])
print(t1)

# tuple within tuple
hero1=("My","Hero","No.","One")
hero2=("You","Are","Not","My","Hero")
new_hero=(hero1,hero2)
print(new_hero)
print(new_hero[0][1])
print(new_hero[1])
print(new_hero[1][3])
print(new_hero[1][4])
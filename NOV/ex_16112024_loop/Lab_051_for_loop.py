#for i in range(1,10,1): --> start,stop-1,and step-how you ,by default value is =1
for i in range(0,10,2):
    print(i)

    for i in range(1, 10, 3):
        print(i)
        #default value of start is 0
        # we can remove the start value
        for i in range(10):
            print(i)

for i in range(-1,-10,-1):
    print(i)
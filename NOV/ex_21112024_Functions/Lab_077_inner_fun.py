def outer_fun():
    var1 = 10
    print(var1)
    def inner1_fun():
        print(var1)

    def inner2_fun():
            var2 = 30
            print(var1)
            print(var2)

    inner2_fun()
    inner1_fun()

        # print(var2)

outer_fun()

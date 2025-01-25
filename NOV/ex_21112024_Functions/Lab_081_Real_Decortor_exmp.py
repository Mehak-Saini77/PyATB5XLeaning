import time


def time_cal_decorator(fun):
    def wrapper():
        start_time = time.time()
        print(start_time)
        fun()
        end_time = time.time()
        print(end_time)
        print(f"Total number of time taken by the function-->{start_time - end_time}")
    return wrapper()



@time_cal_decorator
def test_ui_1():
    print("Add a function time taken by this function 1")
    time.sleep(2)


@time_cal_decorator
def test_ui_2():
    print(" Add a function time taken by this function 2")
    time.sleep(5)


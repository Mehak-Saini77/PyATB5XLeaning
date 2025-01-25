def add_before_ui_after_ui(fun):
    def wrapper():
        print("Before running the UI Test cases")
        print("Start the Browser")
        fun()
        print("Ending running the UI Test cases")
        print("Browser is closed")
    return wrapper()








@ add_before_ui_after_ui
def Test_UI():
    print("I will test the UI")
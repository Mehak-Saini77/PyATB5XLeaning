#Match statement ->similar to switch in java/c++
#Match is used when u have python>3.10

#Match variable:
#case pattern1:
#code block
#case pattern2:
#code block

#Write a program  to ask  the user  which browser he wants to run automation
browser_name=input("Enter the browser name\n")
match browser_name :
    case "firefox":
        print("Starting Firefox !!")
    case "chrome":
       print("Starting chrome !!")
    case "Edge":
       print("Starting Edge !!")
    case _:
       print("Browser Not found")


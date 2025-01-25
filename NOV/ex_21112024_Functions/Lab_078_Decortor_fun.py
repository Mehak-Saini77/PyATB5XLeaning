
def add_extra_security(fun):

      def wrapper():
          print("1.Before function is calling !!")
          print("2.Add Seat built,Take License,Be Attentive full,Don't use Mobile phone")
          fun()
          print("3.After the function call!!")
          print("4.Secure Driving,Leave all the items :)")
      return wrapper()

@add_extra_security
def Ola_Cab():
    print("OLA car is booked ")
    print("Ready for ride")



@add_extra_security
def driving_car():
    print("Normal function")
    print("I am driving car")
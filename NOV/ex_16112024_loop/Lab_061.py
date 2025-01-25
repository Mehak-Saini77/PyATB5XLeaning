#Write a program that prints numbers from 1 to 100 .However ,for multiples of 3,print
#"Fizz" instead of the number ,and for multiples  of 5 ,print "Buzz".For numbers that  are muliples
# multiple of the both 3and 5 print "FizzBuzz." (For ,if)

for i in range (1,101):
   if i % 3 == 0 and i % 5 == 0:
    print(f"FizzBuzz- {i}")
   elif i%3==0 :
    print (f"Fizz-{i}")
   elif i%5==0:
         print(f"Buzz-{i}")


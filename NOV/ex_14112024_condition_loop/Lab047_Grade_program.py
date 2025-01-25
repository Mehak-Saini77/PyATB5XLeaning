#Grade calculator
#Write a program that calculates and display the letter grade
#for a given numerical score (eg.A,B,C,D,E,F)
#Based on the following grading scale
#A:90-100
#B:80-89
#C:70-79
#D:60-69
#F:0-59
score=int(input("Enter the score\n"))
if score >=90 and score <=100:
 print("Grade-A")
elif score >=80 and score <=89 :
 print("Grade-B")
elif score >=70 and score <= 79:
 print("Grade-C")
elif score >= 60 and score <= 69:
 print("Grade-D")
elif score >=100 and score <=-1:
    print("You are Superman!! ,You can't get a grade")
else:
 print("Grade-F")
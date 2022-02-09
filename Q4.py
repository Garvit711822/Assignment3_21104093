#Taking input from user between 4 and 10
grade_points=int(input("Enter a number between 4 and 10 both inclusive:",))
if((grade_points>=4)&(grade_points<=10)):
    if(grade_points==10):
        letter_grade='A+'
        performance='Outstanding'
    elif(grade_points==9):
        letter_grade='A'
        performance='Excellent'
    elif(grade_points==8):
        letter_grade='B+'
        performance='Very Good'
    elif(grade_points==7):
        letter_grade='B'
        performance='Good'
    elif(grade_points==6):
        letter_grade='C+'
        performance='Average'
    elif(grade_points==5):
        letter_grade='C'
        performance='Below Average'
    elif(grade_points==4):
        letter_grade='D'
        performance='Poor'
    print("Your Grade is",letter_grade," and Performance is",performance)
else:
    print("Error! PLease type number only between 4 and 10 both inclusive")
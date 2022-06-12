#Q1

print("Q1\n\n")

def grade(marks):
    z = "Your Grade Is"
    if marks < 25:
        print(f"{z} F")
    elif marks >= 25 and marks < 45:
        print(f"{z} E")
    elif marks >= 45 and marks < 50:
        print(f"{z} D")
    elif marks >= 50 and marks < 60:
        print(f"{z} C")
    elif marks >= 60 and marks < 80:
        print(f"{z} B")
    else:
        print(f"{z} A")


marks = int(input("Enter your Marks: "))
grade(marks)





#Q2

print("\n\n\n\n\nQ2\n\n")

def check_for_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print("It's a leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print("It's a leap year")
    else:
        print("This is not a leap year")


year=int(input("Enter the Year: "))
check_for_leap_year(year)





#Q3

print("\n\n\n\n\nQ3\n\n")

def multiplication():
    import random
    for i in range(1,11,1):
        m=random.randrange(1,10,1)
        n=random.randrange(1,10,1)
        ans=int(input((f"Question {i}: \n{m}*{n} = ")))
        if m*n==ans:
            print("Right!\n")
            continue
        else:
            print("Wrong. The answer is ",m*n ,"\n")
            continue


multiplication()





#Q4

print("\n\n\n\n\nQ4\n\n")
def no_of_candy():
    for i in range(200):
        if i%5==2:
            if i%6==3:
                if i%7==2:
                    print(f"No of candies in the bowl is {i}")


no_of_candy()

# Q1

print("Q1\n\n")


def perfect_number(n):
    s = 0
    for i in range(1, n):
        if (n % i == 0):
            s += i  # Storing the sum of divisors excluding the number itself
    if (s == n):
        return True
    else:
        return False


numb = int(input("Enter a number: "))  # taking user's input
if (perfect_number(numb) == True):
    print(f"{numb} is a perfect number")
else:
    print(f"{numb} is not a perfect number")






# Q2

print("\n\n\n\n\nQ2\n\n")


def palindrome(s):
    s1 = ""
    s1 = s[::-1]
    return s1


string = input("Enter a String: ")
if (palindrome(string) == string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")







# Q3

print("\n\n\n\n\nQ3\n\n")


def factorial(m):
    s = 1
    for i in range(1, m + 1):
        s *= i
    return s


def pascal(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(end=" ")
        for j in range(i + 1):
            # nCr=n!/(r!(n-r)!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

        print()


numb = int(input("Enter a number: "))
pascal(numb)







# Q4

print("\n\n\n\n\nQ4\n\n")


def ispangram(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for character in alphabet:
        if character not in str.lower():
            return False

    return True


user_input = input("Enter a String: ")
if (ispangram(user_input) == True):
    print(f"Yes '{user_input}' is a panagram")
else:
    print(f"No '{user_input}' is not a panagram")







# Q5

print("\n\n\n\n\nQ5\n\n")

string_1 = str(input("Enter a hyphen separated sentence: "))

words = string_1.split("-")
words.sort()

print("-".join(words))







# Q6

print("\n\n\n\n\nQ6\n\n")


def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")
    if "student_name" in kwargs:
        print("Student Name:", kwargs["student_name"])
    if "student_year" in kwargs:
        print("Student Year:", kwargs["student_year"])


student_data(student_id="21102028")
student_data(student_id="21102028", student_name="Inayat Kaur Shah")
student_data(student_id="21102028", student_name="Inayat Kaur Shah", student_year="1st Year")






# Q7

print("\n\n\n\n\nQ7\n\n")


class Student:
    pass


class Marks:
    pass


student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()






# Q8

print("\n\n\n\n\nQ8\n\n")


def findTriplets(arr, n):
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True

    # If no triplet with 0 sum found in array
    if (found == False):
        print("No triplets exist")


list = []
no_element = int(input("Enter number of elements : "))

for i in range(0, no_element):
    ele = int(input())
    list.append(ele)
print(findTriplets(list, no_element))






# Q9

print("\n\n\n\n\nQ9\n\n")


class parantheses:
    def find(str):
        a = ['()', '{}', '[]']
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '')
        return not str


user_input = input("Enter the sequence of parantheses : ")
if parantheses.find(user_input):
    print(user_input, "-", "is balanced")
else:
    print(user_input, "-", "is unbalanced")

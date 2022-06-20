print("Q1\n")

string = input("Enter your string: ")
rev_string=string[::-1]
print(rev_string)





print("\n\n\n\n\nQ2\n")


up_range=int(input("Enter upper range :"))
div_num=int(input("Enter the number that should be divided by..."))
for i in range(1,up_range):
    if i%div_num==0:
        print(i)





print("\n\n\n\n\nQ3\n")


x = float(input('Enter first side: '))  
y = float(input('Enter second side: '))  
z = float(input('Enter third side: '))  

if x > y+z or y > x+z or z > x+y :
     print("\nNo, Triangle can't be formed.")
else:
    s = (x + y + z) / 2  #semi-perimeter

    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5  
    print('The area of the triangle is: ',area)





print("\n\n\n\n\nQ4\n")


n=5
for i in range(n):          #for upward triangle
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n-1):        #for downward triangle
    for j in range (n-1-i):
        print("*", end=" ")
    print()







print("\n\n\n\n\nQ5\n")


n = int(input("Enter number of rows : "))
a=0

for i in range (n):
    for j in range(i+1):
        print(chr(65+a), end="")
        a+=1
    print()







print("\n\n\n\n\nQ6\n")


up_range= int(input('Enter the upper range to find prime numbers till it : '))

for i in range(up_range):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)







print("\n\n\n\n\nQ7\n")


for i in range (1,500):
    if i%7==0 and i%11==0: #to find number multiple of 7 and divisible by 11
        print(i)







print("\n\n\n\n\nQ8\n")


a_list=[]
for i in range(10):
    list_num=int(input("enter number: "))
    a_list.append(list_num)
print(a_list)








print("\n\n\n\n\nQ9\n")


word_list=[]
n=int(input("enter the number of words: "))
for i in range(n):
    word=str(input("Enter the word: "))
    word_list.append(word)

for word in word_list:
    count= word_list.count(word)
    print(word," occurs ",count, " times")


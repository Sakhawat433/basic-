# age=int(input("What is your age? "))
# if age >= 18:
#     print("You are qualified")
# else:
#     print("You can not vote")

# vowel="aeiou"
# letter=input("Input the letter: ")
# letter.lower()
# if letter in vowel:
#     print("It is a vowel")
# else:
#     print("It's a consonant")

# num=int(input("Enter the number"))
# if num % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# num1= int(input("Enter the number 1: "))
# num2= int(input("Enter the number 2: "))
#
# if num1 > num2 :
#     print("Number 1 is greater")
# elif num1==num2 :
#     print("Numbers are equal")
# else:
#     print("Number 2 is greater")


# score = int(input("Enter your score: "))
#
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score <= 89:
#     grade = "B"
# elif 70 <= score <= 79:
#     grade = "C"
# elif 60 <= score <= 69:
#     grade = "D"
# else:
#     grade = "F"
#
# print("The grade is:", grade)
#
# number = float(input("Enter a number: "))
# number = int(number)
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
#
# else:
#     print("The number is zero.")

# age=int(input("Input your age: "))
# GPA= float(input("Input your GPA: "))
# if age < 18:
#     print("You are not eligible")
# elif 17 < age <25 and GPA >=3.5:
#         print("You are Recommended")
# elif 17 < age <25 or GPA >=3.5:
#         print("You are eligible")
# elif age > 24 and GPA >=2.5:
#         print("You are eligible")
# else:
#     print("You are not eligible")
#print even numbers
# L=[1,2,3,4,5,6]
# for i in L:
#     if i%2 == 0:
#         print(i)
#sum of the list
# numbers = [5,10,15,20]
# sum=0
# for num in numbers:
#     sum = sum+num
# print(f"The sum is: {sum}")

vowel= "aeiou"
s= input("Enter a Sentence: ")
s.lower()
count = 0
for i in s:
    if i in vowel:
        count += 1

print(f"Total vowel number is {count}")

# 10 ifelse problem
# 10 for problem
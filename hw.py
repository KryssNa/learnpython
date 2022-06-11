# #(1) If the number is positive or negative,

# # num = float(input("Enter a number: "))
# # if num >= 0:
# #     if num == 0:
# #         print("Zero")
# #     else:
# #         print("Positive number")
# # else:
# #         print("Negative number")



# #(2)to check one,two,three digit number

# a= int(input("enter a number"))
# if a>0 and a<10:
#     print("one digit number")
# elif a>=10 and a<100:
#     print("two digit number")
# elif a>=100 and a<1000:
#     print("three digit number")
# else:
#     print("more than three digit number")


# #(3) given year is leap year or not

# year = int(input("Enter a character to check:"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("Year is a leap year")
# else:
#     print("Year is not a leap year")


# #(4)  to find a maximum no. out of given number

# a,b,c = int(input("Enter a:")),int(input("Enter b:")),int(input("Enter c:"))
# if a>b and a>c:
#     print("a is maximum")
# elif b>a and b>c:
#     print("b is maximum")
# elif c>a and c>b:
#     print("c is maximum")
# else: print("All are equal")

# #(5) to  check triangle is equilateral,isosceles or sclane

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
# if a==b==c:
#     print("Equilateral triangle")
# elif a==b or b==c or c==a:
#     print("isosceles triangle")
# else: print("Scalene triangle")

# #(6) type of variable

# var1 = (input("enter a variable:"))
# if (type(var1) == int):
#     print("Type of the variable is Integer")
# elif (type(var1) == float):
#     print("Type of the variable is Float")
# elif (type(var1) == complex):
#         print("Type of the variable is Complex")
# elif (type(var1) == bool):
#     print("Type of the variable is Bool")
# elif (type(var1) == str):
#     print("Type of the variable is String")
# elif (type(var1) == tuple):
#     print("Type of the variable is Tuple")
# elif (type(var1) == dict):
#     print("Type of the variable is Dictionaries")
# elif (type(var1) == list):
#     print("Type of the variabl is list")
# else:
#     print("Type of variable is unknown")


# #(7)

# age = int(input("enter your age"))
# if (age >= 11):
#   print ("You are eligible to see the Football match.")
#   if (age <= 20 or age >= 60):
#       print("Ticket price is $12")
#   else:
#       print("Tic kit price is $20")
# else:
#     print ("You're not eligible to buy a ticket.")

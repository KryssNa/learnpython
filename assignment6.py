#1. Create a function with variable length of arguments.

# def add(*num):
#     z=num[0]+num[1]+num[2]
#     print(z)
# add(4,6,8,9)

#2. Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it.

# def outer(a,b):
#     def cal(a,b):
#         return a+b
#     add=cal(a,b) + 5
#     return add
# print(outer(5,6))

# def func(a, b):
#     def cal(a,b):
#         return a+b
#     res = cal(a,b) + 5
#     return res
# print(func(4,4)) 


#3. Assign a different name to function and call it through the new name
# Below is the function display_student(name, age).
# Assign a new name show_tudent(name, age) to it and call it using the new name.

# def display_student(name,age):
#     print(name,age)
    
# display_student("kryss",20)

# show_student=display_student
# # print(f"name:{name} age:{age}")
# show_student("kryss",40)


#4. Find the largest item from a given list.
# x=[1,2,3,4,5,6,7,8]


# def x(list):
#     max=list[0]
#     for a in list:
#         if a>max:
#             max=a
#     return max
# print(x([1,2,3,4,5,6,7,8]))


#5. What is the difference between 10 / 3 and 10 // 3?

# a=10
# b=a/3
# c=a//3
# print(b,c)

##10/3 always gives the value in float and 10//3 is floor division which always gives value in integer.


##6. What about two asterisks (**)?

#  (**) define keyword variable length arguments in which arguments is defined by the keywords in the form of key value pair.
  #eg.

# def add(**num):
#     x=num["a"]+num["b"]+num["c"]
#     return x
# print(add(a=2,c=3,b=8))


#7. What is the difference between local and global variables?
#ans:Local variable stores the value inside function whereas global variable stores the value in the module defined in the program or which are declared outside the function.
# local variable is limited only to the function where it is created whereas global variable are available to all the function which are written after it.
# eg.

# a=50                  
# def fun():
#     b=20
#     return a+b
# print(fun())
#  here, in this given example 'a' is global variable and 'b' is local variable.


#8. Write a function called fizz_buzz that takes a number.


# def fizz_buzz(num):
#     if num % 3 != 0 and num % 5 != 0:
#         return num

#     if num % 3 == 0 and num % 5 == 0:

#         return "FizzBuzz"
#     if num % 3 == 0:
#         return "Fizz"
#         return "Buzz"

# number = int(input("Enter a number: "))

# print(fizz_buzz(number))



#9. Write a function for checking the speed of drivers. 
# If speed is less than 70, it should print “Ok”.
# if the speed is 80, it should print: “Warning”.

# def speed_checking(speed):
#     if speed < 70:
#         return 'OK'
#     elif speed< 80:
#         return 'warning'
# speed = int(input("Enter the spped of car:"))
# print(speed_checking(speed))


##10. Write a program that prompts the user to input a positive integer.
# It should then print the multiplication table of that number. 

# def mul():
#     num=int(input("Enter the positive number:"))
#     for i in range(1,11):
#         print(num,"*",i,"=",num*i)
# mul()

# 11. Write a program that prompts the user to input an integer and
# then outputs the number with the digits reversed.
# For example, if the input is 12345, the output should be 54321.

# num= int(input("Enter the number:"))

# for i in num(4,0,-1):
#   print(i(num))


#12.Write a python program that return the number of characters in a string. 
# myList = "Parameter"
# mylist="Parameter"
# print(len(mylist))


##13. Write a Python program to multiply all the numbers in a list using while and for loop.
# Sample list = [8,2,3,-1,7]
# def multiply(numbers):
#   product=1
#   for x in numbers:
#     product*=x
#   return product
# print(multiply((8,2,3,-1,7)))


#14. Write a Python program to sum all the numbers in a list using for loop and while loop.
# Sample list : [8, 2, 3, 0, 7]

# def add(numbers):
#   total=0
#   for i in numbers:
#     total+=i
#   return total
# print(add((8,2,3,-1,7)))


#15. Accept string from the user and display only those characters which are 
# present at an even index.


# strings =input("enter any words:")
# even_str=[]

# for i in range((len(strings))):
#   if i%2==0:
#     even_str.append(strings[i])

# print('Even characters: {}'.format(even_str))


# 16. Accept string from the user and display only those characters which are 
# present at an odd index.

# string=str(input("Enter any words:"))
# odd_str=[]
# for i in range((len(string))):
#   if i%2==1:
#     odd_str.append(string[i])
# print("string present at odd index is ",odd_str)


##17. Sum : 1 to 10 (or any number) using while loop.


# def sum():
#   i=1
#   sum=0
#   while i<=10:
#     sum=sum+i
#     i=i+1
#   print(sum)
# sum()


##18. Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

# list=[1,2,3,4,5,6,7,8,9]
# for x in list:
#   if x%2==0:
#     print(x)

#18. Write a Python program to print the odd numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]


# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#   if i%2!=0:
#     print(i)


##20. Write a program to accept percentage and display the Category according to the  following criteria :
# Percentage	Category
# < 41	                     Failed
# >=41 & <55	Fair
# >=55 & <65	Good
# >=65	                     Excellent


# per= int(input("Enter the percentage:"))

# if per<41:
#   print("Failed")
# elif per>=41 and per<55:
#   print("Fair")
# elif per>=55 and per<65:
#   print("Good")
# else:
#   print("Excellent")

#1.  Write a Python function to multiply all the numbers in a list.
#Sample list = [8,2,3,-1,7]

# def product():
#     list = [8,2,3,-1,7]
#     mul = 1
#     for i in list:
#         mul=mul*i
#     print(mul)
# product()


#2.  Write a Python function to sum all the numbers in a list.
#Sample list : [8, 2, 3, 0, 7]

# def sum():
#     list=[8,2,3,0,7]
#     sum=0
#     for i in list:
#         sum=sum+i
#     print(sum)
# sum()


#3.  Write a python function to find min of three numbers.(no parameter and no return type)

# def parameter():
#     a=int(input("Enter the first number:"))
#     b=int(input("Enter the second number:"))
#     c=int(input("Enter the third number:"))
#     if a<=b and a<=c:
#         print("Minimum number is ",a)
#     elif b<=a and b<=c:
#         print("Minimum number is ",b)
#     else:
#         print("Minimum number is ",c)
# parameter()


#4. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

# def fizz_buzz():
#     num=int(input("Enter the number:"))
#     if num%3==0:
#         print("Fizz")
#     elif num%5==0:
#         print("Buzz")
#     elif num%3==0 and num%5==0:
#         print("FizzBuzz")
#     else:
#         print("num")
# fizz_buzz()


# 5. Create a function that can accept two arguments name and age and print its value.
# def show(name,age):
#     print(f"name:{name}and age:{age}")
# show("kryss","22")



#6. Write a program function to find max of three numbers.(no parameter and no return type)

# def parameter():
#     a=int(input("Enter the first number:"))
#     b=int(input("Enter the second number:"))
#     c=int(input("Enter the third number:"))
#     if a>=b and a>=c:
#         print("Greater number is ",a)
#     elif b>=a and b>=c:
#         print("Greater number is ",b)
#     else:
#         print("Greater number is ",c)
# parameter()


#7. Write a Python function to print the even numbers from a given list. 
#sample: [1,2,3,4,5,6]

# def even_num():
#     list=[1,2,3,4,5,6]
#     for i in list:
#         if i%2==0:
#             print(i)
# even_num()

#8. Write a Python function to print the odd numbers from a given list. 
# sample: [1,2,3,4,5,6]

# def odd_num():
#     list=[1,2,3,4,5,6]
#     for i in list:
#         if i%2==1:
#             print(i)
# odd_num()

#9. Write a Python function that takes a number as a parameter and check the number is prime or not.


# def prime_num():
#     num=int(input("Enter the number:"))
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print("Not a prime number")
#                 break
#         else:
#             print("Prime number")
# prime_num()


#10. Write a function to reverse a string.
# def reverse_string():
#     a="python"
#     for i in range(5,-1,-1):
#         print(a[i],end="")
# reverse_string()


#11. Write a program to create a function that takes two arguments, name and age, and print their value.

# def show(name,age):
#     print(f"name:{name} and age:{age}")
# show(name="kryss",age="22")


#12. Write a program to create function func1() to accept a variable length of arguments and print their value.

# def func1(*num):
#     z=num[0]+num[2]+num[3]
#     print(z)
# func1(1,2,3,4)

# def func1(*num):
#     z=num[0]-num[1]+num[3]
#     print(z)
# func1(1,2,3,4)


#13. Write a program to create function calculation()
# such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.

# def calculation(num1,num2):
#     add=num1+num2
#     sub=num1-num2
#     return add,sub
# print(calculation(30,23))


#14. Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name,salary=9000):
#     print(f"name:{name} and salary:{salary}")
# show_employee("salman")
# show_employee("salam",salary=2000)


#15. Find the largest item from a given list. 
# sample: [4, 6, 8, 24, 12, 2]
# list= [4, 6, 8, 24, 12, 2]
# print(max(list))


##16. Find the smalles item from a given list. 
# sample: [4, 6, 8, 24, 12, 2]

# list= [4, 6, 8, 24, 12, 2]
# print(min(list))



#17. Define a function that accepts roll number and returns whether the student is present or absent.

# def attendance(roll_num):
#     num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#     if roll_num in num:
#         print(f"Roll number {roll_num} is present")
#     else:
#         print(f"Roll number {roll_num} is absent")
# roll_num=int(input("Enter the number:"))
# attendance(roll_num)



#18. Define a function that accepts a number and returns whether the number is even or odd.

# def odd_even():
#     a=int(input("Enter the number:"))
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# odd_even()


#19. Define a function which counts vowels and consonant in a word.

# def count_vowel_consonantc():
#     word=input("Please enter a word: ")
#     vowels=0
#     consonants=0
#     for i in word:
#         if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
#             vowels=vowels+1
#         else:
#             consonants=consonants+1
#     print("The number of vowels:",vowels)
#     print("The number of consonant:",consonants)
# count_vowel_consonantc()



# 20.Define a function that returns Factorial of a number.

# def factorial():
#     num=int(input("Enter the number:"))
#     fac=1
#     i=1
#     while i<=num:
#         fac=fac*i
#         i=i+1
#     print(fac)
# factorial()


#21. Define a function that accepts lowercase words and returns uppercase words.

# def display():
#     a=str(input("Enter the word in lowercase:"))
#     print(a.upper())
# display()


#22. Define a function that accepts radius and returns the area of a circle.

# def area(r):
#     r=float(input("Enter the radius of circle:"))
#     area=3.14*r*r
#     return area
# print(area("r"))
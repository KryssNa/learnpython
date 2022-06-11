##Write a python program to reverse a given list using while loop.
##a=[1,2,3,4]


# a=[1,2,3,4]
# reversed_list=[]
# i=3
# while i>=0:
#     reversed_list.append(a[i])
#     i=i-1
# print("Reversed list is :",reversed_list)


##Write a python program to reverse a string using while loop. a="python"

# a="python"
# reversed_string=[]
# i=5
# while i>=0:
#     reversed_string.append(a[i])
#     i=i-1
# print(reversed_string)


##Write a python program to print a multiplication table of any number using while loop. 

# number=int(input("Enter the number:"))
# i=1
# while i<=10:
#     print(number,"*",i,"=",number*i)
#     i=i+1


##Write a python program to reverse a given list using while loop.

a = [34,35,36,37,38]
reversed_lists=[]

for i in reversed(a):
    reversed_lists.append(a[i])
print(reversed_lists)
# i = 5
# list=len(a)
# while i<list:
#     reversed_lists.append(a[i])
#     i=i-1
# print("Reversed lists is:",reversed_lists)


##Write a program to print the following using while loop
# a. first 10 even numbers

# i = 1

# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

##b.first 10 odd numbers

# i=1
# while i <= 20:
#     if i % 2 == 1:
#         print(i)
#     i = i + 1

##c.first 10 natural numbers

# i=1
# while i <=10:
#     print(i)
#     i = i + 1


##Write for loop statement to print the following series:10 20 30 --------300

# i=10
# while i <=300:
#     print(i)
#     i = i + 10


##7. Write a while loop statement to print the following series:105 98 -------7

# i=105
# while i >=7:
#     print(i)
#     i = i -7


##8. Write a program to print the factorial of a number accepted from user.

# num=int(input("Enter the number:"))
# fac=1
# i=1
# while i <=num:
#     fac= fac*i
#     i=i+1
# print("factorial of",num,"is",fac)
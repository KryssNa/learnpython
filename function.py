# def add():
#     print("hello")
#     print("python")
#     print("python")
#     print("python")
#     print("python")
#     print("python")
#     print("python")
# add()

#print python 5 times


# def add():
#     print("hello")
#     a= 5 * 'python\n'
#     print(a)
# add()



# def add ():
#     x=20
#     y=10
#     c=x+y
#     print(c)
# add()

# def login(username,password):
#     print(f"your username is:{username} and your password is:{password}")
# login("sunil","Battle")

# def login(username,password):
#     print(f"your username is:{username} and your password is:{password}")
# login("kryss","2345")

# def credintials(username,email,address,phoneno,password):
#     print(f"your username is:{username} and your email is:{email} and your address is:{address} and your  phone number is :{phoneno} and your password is :{password}")
# credintials("kryss","kryss@gmail.com","bkt","656456","jkhf655")

# def data(add,sub,mul,div):
    
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b

#     print(f"add is{add}")
# data()


# def data(a,b,c):
#     if a>b and a>c:
#         print(f"greater no. ios:{a}")
#     elif b>c and b>a:
#         print(f"greater no. ios:{c}")
#     else:
#         print(f"greater no. ios:{b}")
# data(10,20,30)



# a=[1,2,3,4]
# sum = 0
# for i in a:
#     sum = sum+i
# print(sum)

# def sum():
#     a=[1,2,3,4]
#     sum = 0
#     for i in a:
#         sum = sum+i
#     print(sum)
# sum()


# a=[1,2,3,4]
# mul= 1
# for i in a:
#     mul= mul*i
# print(mul)

# def product():
#     a=[1,2,3,4]
#     mul= 1
#     for i in a:
#         mul = mul*i
#     print(mul)
# product()


# a = "python"
# for i in range(5,-1,-1):
#     print(a[i], end="")


# def reverse():
#     a = "python"
#     for i in range(5,-1,-1):
#         print(a[i], end="")
# reverse()


# a=[8,9,10,11]
# reversed_list=[]
# for i in reversed(a):
#     reversed_list.append(i)
# print(reversed_list)



# def login(username,password):
#     print(f"your username is:{username} and your password is:{password}")
# login(name="sunil",password =20


# def show(name,age=20):
#     print(f"name:{name} age:{age}")
# show(name="kryss",age=25)

# def show(*num):
#     z=num[0]+num[1]+num[2]
#     print(z)
# show(5,4,3)

# def show(*num):
#     z=num[0]+num[1]+num[2]+num[3]
#     print(z)
# show(5,4,3,2,45,)

# def show(**num):    #####error aauxa
#     z=num['a']+num['b']+num['c']+num['d']+num['e']
#     print(z)
# show(a=5,b=4,c=3,d=5)

# def show(**num):
#     z=num['a']+num['b']+num['c']+num['d']
#     print(z)
# show(a=5,b=4,c=3,d=5)

# def add(x,y,z):
    
#     print(y)
# add(z=5,x=4,y=9)

#variable length arguments

# def show(*num):
#     z=num[0]+num[1]+num[2]
#     print(z)
# show(3,4,5)

# def show(**num):
#     z=num['a']+num['b']+num['c']
#     print(z)
# show(a=5,c=10,b=2)


# def greeter(name):
#     print("good morning")
#     print("hello"+str(name))
# print("go")
# print("world")
# greeter("kryss")

# def add(y):
#     x=10
#     return x+y
# sum=add(20)
# print(sum)

# def add(x,y):
#     sum=x+y
#     sub=x-y
#     return sum,sub
# sum,sub=add(20,10)
# print(sum)
# print(sub)


# def add(x,y,z):
#     a=x+y+z
#     b=x+y-z
#     c=x-y-z
#     return a,b,c
# a,b,c=add(30,20,10)
# print(a,b,c)


# def adding():
#     a=30
#     b=20
#     multi=a*b
#     return multi
# print(adding())

# def add(x,y):
#     sum=x+y
#     return sum
# sum = add(20,10)
# print(sum)


# def addition(x,y):
#     sum=x+y
#     return sum
# print(addition(10,20))


# def add_two(a,b):
#     return a+b
# g=int(input("Enter the first number:"))
# h= int(input("Enter the first number:"))
# c=add_two(g,h)
# print(c)

# def mul_two(a,b):
#     return a*b
# g=int(input("Enter the first number:"))
# h= int(input("Enter the second number:"))
# c=mul_two(g,h)
# print(c)

# def greater_two(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a= greater_two(2,3)
# print(f"greater value is : {a}")


# def greater_value(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if b>a:
#             if b>c:
#                 return b
#             else:
#                 return c
# a=greater_value(2,5,7) 
# print(f"grater value is :{a}")            


# def last_char(a):
#     return a[-1] 
# b=input("enter the word:")
# c=last_char(b)
# print(f"last character is:{c}")     


#practice for function

# def add(y):
#     x=10
#     return x+y
# sum = add(20)
# print(sum)


# def add(x,y):
#     sum=x+y
#     sub=x-y
#     return sum,sub
# # sum,sub=add(20,10)
# print(add(20,10))
# # print(sub)



# def multiplication(a,b):

#     multi=a*b
#     return multi
# print(multiplication(10,20))



# def division(a,b):

#     multi=b/a
#     return multi
# print(division(10,20))


# def multiplication(a,b):

#     multi=a*b
#     division=b/a
#     return multi
# print(multiplication(10,20))

# def add(x,y,z):
#     a=x+y+z
#     b=x+y-z
#     c=x-y-z
#     return a,b,c
# a,b,c=add(30,20,10)
# print(a,b,c)



# def add(x,y):
#     sum=x+y
#     sub=x-y
   
# # sum,sub=add(20,10)
#    print(add(20,10))
# # print(sub)


# def greater_value(a,b,c):
#     a=int(input("Enter the first no.:"))
#     b=int(input("Enter the second no.:"))
#     c=int(input("Enter the third no.:"))
#     if a>b:
#         if a>c:
#             return a
#         else:
#             return c
#     else:
#         if b>a:
#             if b>c:
#                 return b
#             else:
#                 return c
# x=greater_value("a","b","c") 
# print(f"grater value is :{x}")


# def greater_value(a,b,c):
#     a=int(input("Enter the first no.:"))
#     b=int(input("Enter the second no.:"))
#     c=int(input("Enter the third no.:"))

#     if a>b and a>c:
#         return a
   
#     if b>c and b>a:
#         return b
#     else:
#         return c
# x=greater_value("a","b","c")
# print(f"greater value is {x}")





# def disp():
#     def show():
#        return"jshfjjs"
#     result=show()+"disp fum"
#     return result
    
# disp()




# def disp():
#     def show():
#         return "show"
#     result = show()+"disp fumnc"
#     return result
# print(disp())



# def add(**num):
#     z=num['d']+num['c']+num['a']
#     return z
# print(add(a=3,b=4,c=5,d=5))


# def outer(a,b):
#     def inner(a,b):
#         sum=a+b
#         return sum
#     add=inner(a,b)+6
#     return add
# print(outer(4,5))


# def display_student(name,age):
#     print(name,age)
# show_student=display_student
# show_student("kryss",20)

# def x(lists):
#     max=lists[0]
#     for a in lists:
#         if a>max:
#             max=a
#     return max
# print(x([2,3,434,55,5,6,4,4,333,9]))

# def fizzbuzz(num):
#     if num%3!=0 and num%5!=0:
#         return num
#     elif num%3==0:
#         return 'fizz'
#     elif num%5==0:
#         return 'buzz'
# num=int(input("Enter the number"))
# print(fizzbuzz(num))


# num=int(input("Enter the number:"))
# for i in range(1,10):
#     mul=num*i
#     print(num,"*",i,"=",mul)

# i=10
# while i>=1:
#     print(num,"*",i,"=",num*i)
    # i-=1

 
 
 
# sab=("a","e","i","o","u")
 
# string="".join(sab)
# print(string)


# def mul(lists):
#     prd=1
#     for x in lists:
#         prd*=x
#     return prd
# print(mul([2,3,4,5]))


# a=[1,23,4,5,7,8,9]
# reversed_list=[]
# for i in reversed(a):
#     reversed_list.append(a[i])
# print(reversed_list)

# str=input("Enter the words")

# evenstr=[]
# oddstr=[]
# for i in range(len(str)):
#     if i%2!=0:
#         evenstr.append(str[i])
# print(evenstr)




# def x(data):
#     min=data[0]
#     for a in data:
#         if a<min:
#             min=a
#     return min 
# print(x([43,5,4,35,5,74]))


# list1=[22,64,11,345,23,535,444,64,43]

# # list2=list(set(list1))
# # list2.sort()
# # print(list2[-2])

# list2=list1.copy()

# # list2.pop(4)


# print(list2)


# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# odd=0
# even=0

# for i in numbers:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(odd,even)




# tuple1=(22,64,11,345,23,535,444,64,43)
# list1=list(tuple1)
# list1.insert(3,"kryss")
 
# tuple2=tuple(list1)
 
# print(tuple2)

# tuple1=("k","r","y","s","s")
# string="".join(tuple1)
# print(string)


# data=[('Key 1', 1), ('Key 2', 2), ('Key 3', 3)]

# data2=dict(data)


# print(data2)



# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# new_dict=dic1.copy()

# new_dict= update (dic2|dic3)
# print(new_dict)

# data={"name":"kryss",'age':22}

# data2=data.get('name')

# print(data2)


# d=dict()

# for i in range(1,16):
#     d[i]=i**2
# print(d)

# dict1={"name":"kryss","age":20}
# dict2={"address":"ktm","weight":60}

# dict1.update(dict2)
# print(dict1)


# list1=[22,64,11,345,23,535,444,64,43]

# list2=list(set(list1))
# list2.sort()
# print(list2[-3])



# et = set([0, 1, 2, 3, 4, 5])

# for n in et:
#   print(n)



# data={1,2,3,4,5,5,6,7,7}

# data.remove(2)
# print(data)


# data={"name":"kryss","age":20}

# if 'kryss' in data.values():
#     print("pnt")


# from math import *
# a=4
# b=5
# print(sqrt.math(a))

# def add(a,b):
#     return a+b
# g=int(input("ebter"))
# h=int(input("ebter"))
# c=add(g,h)
# print(c)


# def last(a):
#     return a[-1]
# a=input("Enter")
# print(last(a))


# def greater(a,b,c):
#     a=int(input("Enter the no."))
#     b=int(input("Enter the no."))
#     c=int(input("Enter the no."))
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     else:
#         return c
# print(greater("a","b","c"))


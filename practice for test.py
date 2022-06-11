
# def disp():
#     def show():
#         return "show function"
#     result=show() + " desp function"
#     return result
#     show()
# print(disp())

# for i in range(4,0,-1):
#     print(i)

# import pdb
# bike1="yamaha"
# bike1_price=20000

# bike2="Honda"
# bike2_price=25000

# pdb.set_trace()
# name=input("Enter your name:")
# choose=int(input("press 1 for yamaha or press 2 for honda:"))
# print(f"hello {name}")

# if choose==1:
#     print(f"{bike1} will cost you {bike1_price}")
# elif choose==2:
#     print(f"{bike2} will cost you {bike2_price}")
# else:
#     print("press only 1 or2")



# li=[2,3,4,5,6]

# square_list=list(map(lambda x:x**2,li))
# print(square_list)


# def outer(a,b):
#     def c(a,b):
#         cal=a-b
#         return cal
#     add=c(a,b)+5
#     return add
# print(outer(2,3))

# def show_student(name,age):
#     print(name,age)
# # show_student("kryss",40)
# display_student=show_student
# # print(f"name is {name},{age} years")
# display_student("kryss",20)


# def show_student(name,age):
#     print(name,age)
# display_student=show_student
# display_student("kryss",20)

# def x(list):
#     max=list[0]
#     for a in list:
#         if a>max:
#             max=a
#     return max
# print(x([2,3,42,2,5,6,7,8]))



# def x(lists):
#     max=lists[0]
#     for a in lists:
#         if a>max:
#             max=a
#     return max
# print(x([3,44,33,22,56,23,35,77]))


# def x(lists):
#     min=lists[0]
#     for a in lists:
#         if a<min:
#             min=a
#     return min
# print(x([88,44,33,22,56,23,35,77]))



num= int(input("Enter the number:"))

for i in num(4,0,-1):
  print(i(num))

# a='2'
# b= '3'
# r= a+b
# print(r)


# a=[1,2,3,4]
# sum = 0
# for i in a:
#    sum = sum + i
# print(sum)




# i=1
# while i<=11:
#     print(i)
#     i = i + 3


# i=2
# while i<=21:
#     print(i)
#     i = i + 2


# i=1
# while i<=10:
#     print("2","*",i,"=",i*2)
#     i = i + 1

# i=10
# while i>=1:
#     print("2","*",i,"=",i*2)
#     i = i -1

# a=[1,2,3,4]
# sum = 0
# i=0
# lists = len(a)
# while i<lists:
#     sum = sum + a[i]
#     i = i +1
# print(sum)



# a= [9,8,7,6]
# reversed_list=[]
# i=3
# lists = len(a)-1
# while i>=0:
#     reversed_list.append(a[i])
#     i=i-1
# print(reversed_list)

# a=[1,2,3,4,5,6]
# i=1
# sum=0
# lists=len(a)
# while i<lists:
#     sum+=a[i]
#     i=i+1
# print(sum)

# a=[1,2,3,4,5,6]
# reversed_list=[]
# i=5
# lists=len(a)-1
# while i>=0:
#     reversed_list.append(a[i])
#     i=i-1
# print(reversed_list)



# a=[3,3,2,4,1,3,6,3,9]
# i=8
# mul=[]
# prd=len(a)
# while i>=0:
#     mul.append(a[i])
#     i=i-1
# print(mul)


# num=int(input("Enter the number:"))
# i=1
# fac=1
# while i<num:
#     fac*=i
#     i+=1
# print(fac)

# num=int(input("Enter the num:"))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i=i+1



# num=int(input("Enter the number:"))
# i=10
# while i>=1:
#     print(num,"*",i,"=",i*num)
#     i-=1


# a=int(input("Enter the number:"))
# if a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print("not")
#             break
#     else:
#         print("yes")


a=[1,2,3,4,5,6]

reversed_list=[]

i=5

while i>=0:
    reversed_list.append(a[i])
    i-=1
print(reversed_list)
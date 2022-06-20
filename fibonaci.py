# n=int(input("Enter th num:"))
# x=0
# y=1
# z=0
# while (z<=n):
#     print(z,end=",")
#     x=y
#     y=z
#     z=x+y


# n=int(input("Enter th num:"))

# first=0
# sec=1

# for i in range(n):
#     print(first,sep=" ",end=",")
#     temp=first
#     first=sec
#     sec+=temp



# n=int(input("Enter th num:"))


def fac(n):
    if n==1:
        return 1
    else:
        return(n * fac(n-1))
    
    
n=5
print("factorial of",n,"is",fac(n))
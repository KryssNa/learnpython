# y=10
# def outer():
#     z=4
#     def inner():
#         x=5
#         print("x:",x)
#         print("inside the function:",y)
#     inner()
#     print("z", z)
# outer()

# y=10
# def outer():
#     z=4
#     def inner():
#         x=5
#         nonlocal z
#         z=z+1
#         print("x:",x)
#         print("inside the function:",y)
#     inner()
#     print("z", z)
# outer()


# y=10
# def outer():
#     z=4
#     global y
#     y=y+1
#     def inner():
#         x=5
#         # global y
#         # y=y+1
#         print("x:",x)
#         print("inside the function y:",y)
#     inner()
#     print("z:", z)
# outer()

# y=10
# def outer():
#     z=4
#     global y
#     y=y+1
#     def inner():
#         x=5
#         # global y
#         # y=y+1
#         print("x:",x)
#         print("inside the function y:",y)
#         print("z:", z)
#     inner()
#     # print("z:", z)
# outer()


# x=10
# def outer():
#     y=20
#     def inner():
#         x=40
#         print("x:",x)
#         print(y)
#     inner()
#     # print(x)
# print(x)
# outer()


# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("x:",x)
#     inner()
#     print("x:",x)
# outer()
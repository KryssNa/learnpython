
# for i in range(0,5):
#     for j in range(0, i+1):
#         print('*',end="")
#     print()


# rows=5
# for i in range(rows+1,0,-1):
#     for j in range(0, i-1):
#         print('*',end="")
#     print("")




# # It is used to print the space  
# k = rows - 2  
# # Output for downward triangle pyramid  
# for i in range(rows, -1, -1):  
#     # inner loop will print the spaces  
#     for j in range(k, 0, -1):  
#         print(end=" ")  
#     # Increment in k after each iteration  
#     k = k + 1  
#     # This inner loop will print number of stars  
#     for j in range(0, i + 1):  
#         print("* ", end="")  
#     print("")  


# rows = 7  
# # Outer loop will print the number of rows  
# for i in range(0, rows):  
#     # This inner loop will print the stars  
#     for j in range(0, i + 1):  
#         print("*", end=' ')  
#     # Change line after each iteration  
#     print(" ")  
# # For second pattern  
# for i in range(rows + 1, 0, -1):  
#     for j in range(0, i - 1):  
#         print("*", end=' ')  
#     print(" ")  



# rows = int(input("Enter the number of rows: "))  
# for i in range(1, rows + 1):  
#     for j in range(1, rows + 1):  
#         # Check condition if value of j is smaller or equal than  
#         # the j then print i otherwise print j  
#         if j <= i:  
#             print(i, end=' ')  
#         else:  
#             print(j, end=' ')  
#     print()  


# rows = int(input("Enter the number of rows: "))  
# for i in range(1, rows + 1):  
#     for j in range(1, rows + 1):  
#         # Check condition if value of j is smaller or equal than  
#         # the j then print i otherwise print j  
#         if j <= i:  
#             print("*", end=' ')  
#         else:  
#             print("*", end=' ')  
#     print()  
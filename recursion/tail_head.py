# Types of recurssion: 
#   • Head Recurssion 
#   • Tail Recurssion
#   • Tree Recurssion
#   • Indirect Recurssion #

#   • Tail Recurssion
# def calculate_rec(n):
#     if n > 0:
#         k = n ** 2
#         print(k)
#         calculate_rec(n - 1)

# calculate_rec(4)  

#   • Head Recurssion 
# def calculate_rec(n):
#     if n > 0:
#         calculate_rec(n - 1)
#         k = n ** 2
#         print(k)

# calculate_rec(4)  

#   • Tree Recurssion
def calculate_rec(n):
    if n > 0:
        calculate_rec(n - 1)
        k = n ** 2
        print(k)
        calculate_rec(n - 1)

calculate_rec(3)  

# Indirect:
# def calculate_B(n):
#     if n > 0:
#         ...
#         calculate_A(n)

# def calculate_A(n):
#     if n > 0:
#         ...
#         calculate_B(n)
        

calculate_rec(4) 
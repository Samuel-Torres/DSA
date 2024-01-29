# get inputs from user: with input():

# x = input("Type anything:")
# print("The user typed: ", x)
# print(type(int(x)))

def addNums(a: int, b: int):
    return a + b

# add two numbers:

num1 = input("insert first number: " )
num2 = input("insert second number: " )

print(addNums(int(num1), int(num2)))

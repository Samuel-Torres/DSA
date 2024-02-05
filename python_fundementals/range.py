# range is a function that generates a range of integers. 

# range(0, 5) & range(5) --> 0, 1, 2, 3, 4
# range(5, 10) --> 5, 6, 7, 8, 9

# you can index & splice with range:

# range can have 3 params:
# range(0, 10, 2) --> (initial num, until -1, incriment by num) --> 0, 2, 4, 6 , 8
# range(0, 10, -1) --> (initial num, until -1, incriment by num) --> 10, 9, 8, ... 1


x = range(5)
print(x)
print(x[0]) # --> 0
# print(x[5]) # --> out of range

print(id(x[0]))
print(id(x[0]))

# range datatype is immutable
x[0] = 10 # --> will cause error because range function items are immutable. NOT WORKING: Investigate
print(id(x[0]))





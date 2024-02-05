my_var = 10
print(my_var)

# difference between dynamically types and statically typed data types:
# Python data types are dynamically typed and determined at runtime. 
# when you declare a variable no type is defined. "my_var" is not "int my_var".

# In Python everything is an object. 

x = 10 # --> declaration.
type(x) # --> returns <type 'int'>
id(x) # --> shows it's location in state within an object. return address.
print(x) # returns the value of the variable within the object.

print(id(x))

# Assigning declaring and assigning values to multiple variables. 

x, y, z = 1, 2, 3 # x assigns to 1, y assigns to 2, z assigns to 3. 
print(x, y, z) # returns -> (1, 2, 3)

new_var = 20
print(new_var) # value is 20 
print(my_var) # value is 10 

# when assigning the value of one variable to the value of the other in memory the return address points to
# to the same location in memory. Above 'my_var' & 'new_var' currently point to different locations in memory.

# test: 

print(id(my_var)) # prints: 140247667069184
print(id(new_var)) # prints: 140377672668368

# these two variables point at different locations in memory at the moment. But, when assigning the 
# valye of new_var to my_var they will point at the same location in memory hence the values are literally
# the same exact value instance.


new_var = my_var

print(new_var) # returns 10
print(id(new_var)) # returns 140247667069184

# this is a function of numbers in python being immutable.
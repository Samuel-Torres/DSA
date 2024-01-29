# Booleans are True & False: type represented as <type 'bool'> or bool.
# boolean type True is respresented as 1, while False is represented as 0

print(type(True)) # returns <type 'bool'>.

x = True
print(x) # returns True

x = 10
y = 20
z = x > y

print(type(x)) # returns: <type 'int'>
print(type(y)) # returns: <type 'int'>
print(type(z)) # returns: <type 'bool'>
print(z) # returns: False

# NONE:
num = 10
print(num) # 10
print(type(num)) # <type 'int'>
num = None
print(num) # None
print(type(num)) # <type 'NoneType'>
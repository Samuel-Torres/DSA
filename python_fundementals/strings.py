s = "Hello" # <type 'str'>


print(s)
print(type(s))

# to have a string with apostrophe needs to have double quoted string first. 
# 'It's cold outside' would throw syntax error below. 
# string = 'it's cold outside'
# print(string)

# proper way to write string below:
string = "it's cold outside"
print(string)


# Multi-line strings can not be delimitted. In order to break strings into separate lines you would need
# to use triple single quotes. Example:

# line_one = 'This is first line,
#     this is second line, 
#     this is third line.
# '

# above string will throw an error. correct way below:
# doc strings:

line_two = '''This is first line,
    this is second line, 
    this is third line.
'''

# print(line_one) # SyntaxError: EOL while scanning string literal
print(line_two) # returns: 
# This is first line,
    # this is second line, 
    # this is third line.

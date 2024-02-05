# Dictionaries: 
# have key/val pairs
# unordered data structure
# Instead of indices it uses key
# keys in dictionaries are immutable
# Keys must be unique
# keys are case sensitive#

# Example: 
dict = { "key": 'val', "key1": 2, "key2": (1, 2)}

# Accessing items in a dictionary:
print(dict["key2"])

# Adding to a dictionary:
dict["key3"] = 2.41
print(dict)

# Deleting from dictionary:
del(dict["key3"])
print(dict)

# getting the keys of a dictionary:
print(dict.keys())

# getting the values of a dictionary:
print(dict.values())

# getting the length of a dictionary:
print(len(dict))

# Checking for items in Dictionary: only works on keys
print("key2" in dict)

d = { 
    "USA": 100,
    "UK": 200,
    "India": 300,
}

print(d[0])
print(len(d))
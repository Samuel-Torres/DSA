# Tuples are an ordered sequence of data 
# Tuples are immutable as String
# tuple ex: tup = ( 1, 2, 3, 4, 5) #
tup1 = (1, 2, 3)

# accessing elements in tuple: 
    # tup[0] -- 0 based indexing  

print("Returns 2: ", tup1[1])

# concatonating tuple: 
# tup2 = tup1 + (6, "New Item") ---> (1, 2, 3, 4, 5, 6, "New Item") #
tup2 = tup1 + (4, "New item")
print("Prints: , (1, 2, 3, 4, 'New item')", tup2)

# Since items are immutable cannot change "New Item" to "Hello"
# tup2[4] = "Hello" # returns --> TypeError: 'tuple' object does not support item assignment

# can slice tuples:
print("Prints: (1, 2, 3): ", tup2[0:3])

# get length:
print(len(tup2))
print(min(tup2))
print(max(tup2))
print(2 in tup2)
print(2 not in tup2)
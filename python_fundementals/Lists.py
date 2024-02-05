# Lists are a data structure in Python:
    # Lists are mutable
    # Lists are an ordered sequence of data.


# Ways to alter

# concatonating lists:
# Approach below appends the concatonated items into the new list.
# L1 = [10, 'Hello', 2.85]
# L2 = L1 + [56.2, "Python"]
# print(L2)

# array methods:

list1 = [1, 2, 4, 5, 6, 7]

# array.insert(index of where to insert, element to insert) # adds item to specified location.
list1.insert(0, 0)
print("Inserted 0 to the first index: ", list1)
# array.append() # appends to the end
list1.append(8)
print("appended 8 to the list: ", list1)
# array.extend(takes list as argument [2 , 4]) appends item to the list.
list1.extend([9, 10])
print("extended array with two items '9 and 10': ", list1)
# array.del(array[index]) removes item in specified array & index.
del(list1[-1])
print("Deleted last item '10' from array: ", list1)


# slicing:
# array[0:3] gets the items in the specified range - 1.
new_list = list1[0:3]
print("Grabbed indices 0, 1, 2 from array resulting in '[0, 1, 2]': ", new_list)
# array2 = array1[:] <-- if range not specified will copy entire array into new array. 
new_list2 = list1[:]
print("Grabbed entire array and made a copy of array in new_list: ", new_list2)


string = "My String"
# convert string to list: string.split()
# string = 'my string'
# string.split() --> ['my', 'string']
new_string = string.split()
print("converted string to array: ", new_string)

string2 = "20,10,40,30"
# can use delimitter to split strings also:
# string = "10,20,30,40" delimitter is comma. 
# string.split(",") ---> ['10', '20', '30', '40']
arr = string2.split(",")
print("converted string to array split at every comma: ", arr)

num_arr = [int(i) for i in arr]

print("convert to integer array: ", num_arr)

# sort method:
# array.sort() --> arranged items in array in asc order. Only applied to lists with same types. 
num_arr.sort()
print("sorted asc array: ", num_arr)


# reverse method:
# array.reverse() --> reverses array order of array with like types. 
num_arr.reverse()
print("revered array: ", num_arr)

# get array length:
# array.len() --> returns length of array.
print("array length: ", len(num_arr))

# sum:
# array.sum --> returns sum of all the elements within the array.
print("Sum of array: ", sum(num_arr))

# min:
# array.min --> returns smallest element in array.
print("Smallest item in array: ", min(num_arr))

# max:
# array.max --> returns larges element in array
print("Largest item in array: ", max(num_arr))

# in keyword: checks if element is in specified array if it is then results in True likewise False.
print("50 in num_array should be False", 50 in num_arr)
print("40 in num_array should be True", 40 in num_arr)
# inverse not key returns opposite of in.
print("50 not in num_array should be True", 50 not in num_arr)
print("40 not in num_array should be False", 40 not in num_arr)


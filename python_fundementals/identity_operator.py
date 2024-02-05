L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4]
L3 = [11, 22, 33, 14]
L4 = [4, 1, 2, 3]

print(L1 is L2) # returns False because the id of memory allocation is different for each list. Compared memory id allocation.
print(L1 == L2) # returns True because they are similar though not the same the result is truthy. Compare contect. 
print(L1 == L3) # returns False because items in list are different. 
print(L1 == L4) # returns False because items in list are different though contains same numbers position matters
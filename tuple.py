import copy

# tuple does not support item assignment
# tuple is immutable but we can add list in tuple which will be mutable

## Normal Tuple


# tuple1 = (1, 2, 3, 4)

# assignment operator --> creates shallow copy

# s_copy=tuple1
# print(s_copy)
# print(tuple1)

# copy --> since tuple is immutable so there is no use of it

# d_copy = copy.copy(tuple1)
# print(d_copy)
# print(tuple)


## Nested tuple --> Set with list inside

tuple1 = ([1, 2], 3, 4, 5)

# assignment operator --> creates shallow copy

# s_copy=tuple1
# s_copy[0][0]=9
# print(s_copy)
# print(tuple1)

# copy --> creates shallow copy of inner list and outer tuple is immutable

# d_copy = copy.copy(tuple1)
# d_copy[0][0] = 9
# print(d_copy)
# print(tuple1)

# deepcopy --> creates deep copy of inner list

# d_copy = copy.deepcopy(tuple1)
# d_copy[0][0] = 9
# print(d_copy)
# print(tuple1)

# In this copy and deepcopy has same property as list

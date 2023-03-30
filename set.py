import copy
# Set does not support item assignment
# it can add ,delete and other operation except update on index
# in nested set it can have only immutable values like string, tuple

## Normal Set

# set = {1, 2, 3, 4}

# assignment operator --> creates shallow copy

# s_copy=set
# s_copy.add(6)
# print(s_copy)
# print(set)

# copy --> creates deep copy of set

# d_copy = copy.copy(set)
# d_copy.add(6)
# print(d_copy)
# print(set)


## Nested Set

# set1 = {(1, 2), (3, 4), (5, 6)}

# assignment operator --> creates shallow copy

# s_copy=set1
# s_copy.add((9,6))
# print(s_copy)
# print(set1)

# copyfunction --> creates deep copy of outer set and inner tuple is immutable so
#                  there is no use of it

# d_copy=copy.copy(set1)
# d_copy.add((9,6))
# print(d_copy)
# print(set1)


# deepcopy --> creates deep copy of set it works same as copy

# d_copy=copy.deepcopy(set1)
# d_copy.add((9,6))
# print(d_copy)
# print(set1)


# in set copy and deepcopy are same no change

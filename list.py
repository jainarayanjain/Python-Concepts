import copy

list = [1, 2, 3, 4]

# Normal List

# assignment operator --> creates shallow copy of list
#
# s_copy=list
# s_copy[0]=6
# print(s_copy)
# print(list)

# copy --> creates deep copy of list

# d_copy = copy.copy(list)
# d_copy[0]=6
# print(d_copy)
# print(list)


## Nested List

# list=[ [1,2], [3,4], [5,6] ]

# assignment operator --> creates shallow copy of list

# s_copy=list
# s_copy[0][0]=9
# print(s_copy)
# print(list)

# copy --> creates deep copy of outer list and shallow copy of inner list
#     d_copy=copy.copy(list)
#     d_copy[0][0]=9
#     print(d_copy)
#     print(list)

# deepcopy --> creates deep copy of nested and outer list

# d_copy=copy.deepcopy(list)
# d_copy[0][0]=9
# print(d_copy)
# print(list)

import copy

## Normal Dictionary


# dict = {"A":1,"B":2,"C":3}

# assignment operator --> creates shallow copy of dict

# s_copy=dict
# s_copy["A"]=10
# print(s_copy)
# print(dict)

# copy --> creates deep copy of dict

# d_copy = copy.copy(dict)
# d_copy["A"]=10
# print(d_copy)
# print(dict)


## Nested Dict

dict1 = {
    "item1": {"A": 1},
    "item2": {"B": 2},
    "item3": {"C": 3},
    "item4": 5
}

# assignment operator --> creates shallow copy

# s_copy=dict1
# s_copy["item1"]["A"]=6
# print(s_copy)
# print(dict1)

# copy --> creates deep copy of outer dict and shallow copy of inner dict

# d_copy = copy.copy(dict1)
# d_copy["item1"]["A"] = 6
# d_copy["item5"] = 9
# print(d_copy)
# print(dict1)

# deepcopy --> creates deep copy of both outer and shallow dict

# d_copy = copy.deepcopy(dict1)
# d_copy["item1"]["A"] = 6
# d_copy["item5"] = 9
# print(d_copy)
# print(dict1)


# In this copy and deepcopy has same property as list

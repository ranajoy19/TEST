import copy

old_list = [[1,2,4,5],[3,4,5,6],[1,4,3]]

shallow_copy = copy.copy(old_list)
shallow_copy[0][0]= 2
print(shallow_copy)
print(old_list)

# deep_copy = copy.deepcopy(old_list)
# deep_copy[0][0]=6

# print(deep_copy)
# print(old_list)
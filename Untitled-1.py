def get_last_element(t):
    return t[-1]

def sort_tuple_list(tuple_list):
    return sorted(tuple_list, key=get_last_element)

# example usage
tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_tuple_list(tuple_list)
print(sorted_list)

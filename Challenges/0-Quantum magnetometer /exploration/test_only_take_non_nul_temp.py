my_list = [10, 5, 8, 30, 15, 30, 40,40]

# Find the maximum value in the list
max_value = max(my_list)

# Find the indices of all occurrences of the maximum value
max_indices = [index for index, value in enumerate(my_list) if value == max_value]

print("Maximum Value:", max_value)
print("Indices of Maximum Value:", max_indices)

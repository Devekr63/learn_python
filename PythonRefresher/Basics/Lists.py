list_of_numbers = [20, 76, 32, 88]

print(list_of_numbers)

print(list_of_numbers[2])

#negative indexing the list
print(list_of_numbers[-1])
print(list_of_numbers[-3])

print(len(list_of_numbers))

# slicing the list
print(list_of_numbers[0:2])
print(list_of_numbers[-3:-1])

# appending the list
list_of_numbers.append(100)
print(list_of_numbers)

# removing item from the list
list_of_numbers.pop(1)
print(list_of_numbers)

# inserting at index in a list
list_of_numbers.insert(2, 101)
print(list_of_numbers)

# removing the item from a list
list_of_numbers.remove(101)
print(list_of_numbers)

#Sorting the list
list_of_numbers.sort()
print(list_of_numbers)